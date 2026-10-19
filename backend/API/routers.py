from typing import Annotated

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import Json

from DB.models import ExercisesMod, TrainersMod
from files import save_file
from repo import ExercisesRepoSchema, TrainersRepoSchema

router_exercises = APIRouter(tags=["Exercises"], prefix="/exercises")
router_trainers = APIRouter(tags=["Trainers"], prefix="/trainers")

@router_exercises.post("/admin/new")
async def new_exercise(repo: ExercisesRepoSchema, data: ExercisesMod):
    result = await repo.add_exercise(data)
    if not result:
        raise HTTPException(500, detail="asdas")
    return {"exercise_id": result}

@router_exercises.post("/admin/add_foto")
async def add_foto(repo: ExercisesRepoSchema,id:int, file: UploadFile = File(...)):
    file_path = await save_file(file)
    result = await repo.add_exercise_filepath(file_path, "picture_path", id)

    if not result:
        raise HTTPException(500, detail="asdasdasdaddass")

    return {"Status": "Ok"}

@router_exercises.post("/admin/add_video")
async def add_video(repo: ExercisesRepoSchema,id:int, file: UploadFile = File(...)):
    file_path = await save_file(file)
    result = await repo.add_exercise_filepath(file_path, "video_path", id)
    
    if not result:
        raise HTTPException(500, detail="asdasdasdaddass")

    return {"Status": "Ok"}

@router_exercises.get("")
async def get_exercise_by_id(repo: ExercisesRepoSchema, id: int):
    result = await repo.get_exercise_to_id(id)

    if not result:
        raise HTTPException(500, detail="asdasdasdaddas343243243243s")

    return result

@router_exercises.get("/filter_by/level")
async def get_exercises_by_level(repo: ExercisesRepoSchema, level: int):
    result = await repo.get_exercise_to_level(level)

    if not result:
        raise HTTPException(500, detail="asdasdasdaddas343243232323rsadasdasdasdsddddddsdddd43243s")

    return result

@router_exercises.get("/filter_by/name")
async def get_exercises_by_name(repo: ExercisesRepoSchema, name: str):
    result = await repo.get_exercise_to_level(str)

    if not result:
        raise HTTPException(500, detail="asdasdasdaddas343243232323rsadasdasdasdsddddddsdddd43243s")

    return result

@router_trainers.post("/admin/new")
async def add_trainer(repo: TrainersRepoSchema, data: TrainersMod):
    result = await repo.add_trainer(data)

    if not result:
            raise HTTPException(500, detail="a34s")
    
    return {"trainer_id": result}

@router_trainers.post("/admin/add_foto")
async def add_trainer_foto(repo: TrainersRepoSchema,id:int, foto : UploadFile = File(...)):
    foto_path = await save_file(foto)
    result = await repo.add_trainer_foto(foto_path=foto_path, id= id)

    if not result:
            raise HTTPException(500, detail="a34123456789090abobas")
    
    return {"Status": "Ok"}

@router_trainers.get("/all")
async def add_trainer(repo: TrainersRepoSchema):
    result = await repo.get_all_trainers()

    if not result:
            raise HTTPException(500, detail="a3423432432423423s")
    
    return result

@router_trainers.get("")
async def get_trainer_by_id(repo: TrainersRepoSchema, id:int):
    result = await repo.get_trainer_by_id(id)

    if not result:
            raise HTTPException(500, detail="a3423432432423423s")
    
    return result