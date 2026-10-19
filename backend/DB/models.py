from pydantic import BaseModel

class ExercisesMod(BaseModel):
    name: str
    discription: str
    level: str

class ExercisesFotoMod(BaseModel):
    name: str
    discription: str
    level: str
    picture_path: str