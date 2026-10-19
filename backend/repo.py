from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from DB.databases import get_session
from DB.repository import ExercisesRepo


def get_exercises_repo(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return ExercisesRepo(session)



ExercisesRepoSchema = Annotated[ExercisesRepo, Depends(get_exercises_repo)]

