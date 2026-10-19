from contextlib import asynccontextmanager
from pathlib import Path
import os
import uuid
from fastapi import FastAPI,  UploadFile, File, Depends
from fastapi.staticfiles import StaticFiles
from DB.databases import create_all, drop_all
from DB.models import ExercisesMod
from sqlalchemy.ext.asyncio import AsyncSession

from files import UPLOAD_DIR
from API.routers import router_trainers, router_exercises

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("dropping all tables")
    await drop_all()
    print("creating all tables")
    await create_all()
    yield
    print("App stopped")



app = FastAPI(
    lifespan=lifespan
)


BASE_DIR = Path(__file__).resolve().parent


STATIC_DIR = BASE_DIR / "static"


os.makedirs(STATIC_DIR / "uploads", exist_ok=True)


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(router_exercises)
app.include_router(router_trainers)


