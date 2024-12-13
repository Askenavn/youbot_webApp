from fastapi import FastAPI
from contextlib import asynccontextmanager
from router import target_router, youbot_manage_router, youbot_velocity_router
from database import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    await create_tables()
    print("База создана")
    yield
    print("База удалена")

app = FastAPI(lifespan=lifespan)
app.include_router(router=target_router)
app.include_router(router=youbot_manage_router)
app.include_router(router=youbot_velocity_router)


# curl -X 'PUT' \
#   'http://192.168.0.7:8000/cmd_vel/?aruco_id=1&x=0.1&y=0&theta=0' \
#   -H 'accept: application/json'
