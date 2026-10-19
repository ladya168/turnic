from fastapi import APIRouter, File, UploadFile

from DB.models import ExercisesMod
from files import save_exercise
from repo import ExercisesRepoSchema

router = APIRouter()


@router.post()
async def add_exercise(data: ExercisesMod , repo: ExercisesRepoSchema, foto: UploadFile = File(...)):
    foto_path = save_exercise(foto)

    result = repo.add_exercise(data, picture_path = foto_path)






    

