from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from DB.databases import Exercises
from DB.models import ExercisesFotoMod, ExercisesMod






class ExercisesRepo:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def add_exercise(self, data: ExercisesFotoMod):
        data_d = data.model_dump()

        query = Exercises(**data_d)

        self.session.add(query)
        await self.session.commit()
        await self.session.refresh(query)
        if not query.id:
            return None

        return query.id

    # async def get_exercise_to_id(self, id: int):
    #     query = select(Exercises).where(Exercises.id == id)
    #     result = await self.session.execute(query)

    #     db_product = result.scalar_one_or_none()

    #     if not db_product:
    #         return None

    #     return ExercisesMod.model_validate(db_product)

    # async def get_exercise_to_level(self, level: int):
    #     query = select(Exercises).where(Exercises.level == level)
    #     result = await self.session.execute(query)

    #     db_product = result.scalars().unique().all()

    #     if not db_product:
    #         return None

    #     return [
    #     ExercisesMod.model_validate(product)
    #     for product in db_product
    # ]

        