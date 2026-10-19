from pydantic import BaseModel, ConfigDict

class ExercisesMod(BaseModel):
    name: str
    discription: str
    level: int
    

class ExercisesFotoMod(BaseModel):
    name: str
    discription: str
    level: int
    picture_path: str | None
    model_config = ConfigDict(from_attributes=True)


class ExercisesAllMod(BaseModel):
    name: str
    discription: str
    level: int
    picture_path: str | None
    video_path: str | None
    model_config = ConfigDict(from_attributes=True)

class TrainersAllMod(BaseModel):
    name: str
    discription: str
    foto_path: str | None
    price: float
    model_config = ConfigDict(from_attributes=True)

class TrainersMod(BaseModel):
    name: str
    discription: str
    price: float
    model_config = ConfigDict(from_attributes=True)
