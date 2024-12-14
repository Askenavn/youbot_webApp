from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    "sqlite+aiosqlite:///youbot.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class YoubotOrm(Model):
    __tablename__ = 'youbots_cur'
    id: Mapped[int] = mapped_column(primary_key=True)
    aruco_id: Mapped[int]
    arm_count: Mapped[int]


class YoubotTargetOrm(Model):
    __tablename__ = 'youbots_target'
    id: Mapped[int] = mapped_column(primary_key=True)
    aruco_id: Mapped[int] 
    x: Mapped[float] 
    y: Mapped[float] 
    z: Mapped[float] 
    w: Mapped[float] 


class YoubotVelocityORM(Model):
    __tablename__ = 'youbot_velocities'
    id: Mapped[int] = mapped_column(primary_key=True)
    aruco_id: Mapped[int] 
    x: Mapped[float]
    y: Mapped[float]
    theta: Mapped[float]


class TargetFigureORM(Model):
    __tablename__ = 'figures'
    id: Mapped[int] = mapped_column(primary_key=True)
    aruco_id: Mapped[int]
    name: Mapped[str]
    
   
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)