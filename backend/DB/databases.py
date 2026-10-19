from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from config import settings

engine = create_async_engine(settings.db_url_sqlite)
Session_maker = async_sessionmaker(engine)

async def get_session():
    async with Session_maker() as s:
        yield s


class Base(DeclarativeBase):
    pass

class Exercises(Base):
    __tablename__ = "Exercises"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    discription: Mapped[str]
    level: Mapped[int]
    video_path: Mapped[str | None] = mapped_column( nullable=True)
    picture_path: Mapped[str | None] = mapped_column( nullable=True)


class Trainers(Base):
    __tablename__ = "Trainers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    discription: Mapped[str]
    foto_path: Mapped[str | None] = mapped_column( nullable=True)
    price: Mapped[float]





async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)