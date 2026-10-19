from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from DB.databases import get_session
from DB.repository import ExercisesRepo, TrainersRepo


def get_exercises_repo(session: AsyncSession = Depends(get_session)) -> ExercisesRepo:
    return ExercisesRepo(session)
def get_trainers_repo(session: AsyncSession = Depends(get_session)) -> TrainersRepo:
    return TrainersRepo(session)



TrainersRepoSchema = Annotated[TrainersRepo, Depends(get_trainers_repo)]


ExercisesRepoSchema = Annotated[ExercisesRepo, Depends(get_exercises_repo)]

