from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from DB.databases import Exercises, Trainers
from DB.models import ExercisesAllMod, ExercisesMod, TrainersAllMod, TrainersMod


class ExercisesRepo:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def add_exercise(self, data: ExercisesMod):
        if (await self.session.execute(
            select(Exercises.id)
            .where(Exercises.name == data.name))
             ).scalar_one_or_none():
                    return None
        data_d = data.model_dump()

        query = Exercises(**data_d)

        self.session.add(query)
        await self.session.commit()
        await self.session.refresh(query)
        if not query.id:
            return None

        return query.id

    async def add_exercise_filepath(self, file_path: str,file_type: str, id: int):
        data = await self.session.get(Exercises, id)

        if not data:
            return None

        setattr(data, file_type, file_path)

        await self.session.commit()
        await self.session.refresh(data)
        return True


    async def get_exercise_by_id(self, id: int):
        query = select(Exercises).where(Exercises.id == id)
        result = await self.session.execute(query)

        db_product = result.scalar_one_or_none()

        if not db_product:
            return None

        return ExercisesAllMod.model_validate(db_product)

    async def get_exercise_by_level(self, level: int):
        query = select(Exercises).where(Exercises.level == level)
        result = await self.session.execute(query)

        db_product = result.scalars().unique().all()

        if not db_product:
            return None

        return [
        ExercisesAllMod.model_validate(product)
        for product in db_product
    ]
    async def get_exercise_by_name(self, name: str):
        query = select(Exercises).where(Exercises.level == str)
        result = await self.session.execute(query)

        db_product = result.scalars().unique().all()

        if not db_product:
            return None

        return [
        ExercisesAllMod.model_validate(product)
        for product in db_product
    ]

class TrainersRepo:

    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def add_trainer(self, data: TrainersMod):
        if (await self.session.execute(
                    select(Trainers.id)
                    .where(Trainers.name == data.name))
                     ).scalar_one_or_none():
                            return None
        data_d = data.model_dump()

        query = Trainers(**data_d)

        self.session.add(query)
        await self.session.commit()
        await self.session.refresh(query)
        if not query.id:
            return None

        return query.id

    async def add_trainer_foto(self, foto_path: str, id: int):
        data = await self.session.get(Trainers, id)

        if not data:
            return None

        setattr(data, "foto_path", foto_path)

        await self.session.commit()
        await self.session.refresh(data)
        return True
    
    async def get_all_trainers(self):
        query = select(Trainers)
        result = await self.session.execute(query)

        db_product = result.scalars().unique().all()

        if not db_product:
            return None

        return [
        TrainersAllMod.model_validate(product)
        for product in db_product
    ]

    async def get_trainer_by_id(self, id: int):
        query = select(Trainers).where(Trainers.id == id)
        result = await self.session.execute(query)

        db_product = result.scalar_one_or_none()

        if not db_product:
            return None

        return TrainersAllMod.model_validate(db_product)


    
        