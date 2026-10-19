import os
import uuid
from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.staticfiles import StaticFiles
from DB.models import ExercisesMod
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()


UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/upload-video/")
async def upload_video(
    file: UploadFile = File(...), 
    db: AsyncSession = Depends(get_db)  ):
    
    new_media = ExercisesMod(picture_path=server_file_path)
    
    return {
        "id": new_media.id, 
        "file_path": new_media.file_path,
        "url": f"http://127.0.0{server_file_path}"
    }