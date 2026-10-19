from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


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
    level: Mapped[str]
    video_path: Mapped[str | None] = mapped_column( nullable=True)
    picture_path: Mapped[str] 


