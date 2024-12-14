from fastapi import APIRouter, Depends

from schemas import SYoubotTargetAdd, SYoubotCurAdd, SVelocityTargetAdd, SFigureAdd
from repository import YoubotTargetRepository, YoubotRepository, YoubotVelocityRepository



#@@@@@  TARGETS  @@@@@#
target_router = APIRouter(
    prefix='/target',
    tags=['Target']
)

@target_router.post("/")
async def add_target(target: SYoubotTargetAdd = Depends()):
    target_id = await YoubotTargetRepository.add_target(target)
    return {"ok": True, "id": target_id}

@target_router.get("/{aruco_id}")
async def get_target(aruco_id: int,):
    target= await YoubotTargetRepository.find_target(aruco_id)
    return {*target}

@target_router.get("/")
async def get_all_targets():
    targets = await YoubotTargetRepository.find_all_targets()
    return {*targets}

@target_router.post("/figure/")
async def add_figure(aruco_id: int, figure: SFigureAdd = Depends()):
    return await YoubotTargetRepository.add_figure(aruco_id, figure)

@target_router.put("/figure/")
async def add_figure(aruco_id: int, figure: SFigureAdd = Depends()):
    return await YoubotTargetRepository.set_new_figure(aruco_id, figure)

@target_router.get("/figure/")
async def get_figure(aruco_id: int = None):
    return {*await YoubotTargetRepository.get_figures(aruco_id)}
#@@@@@  TARGETS  @@@@@#




#@@@@@  YOUBOTS  @@@@@#
youbot_manage_router = APIRouter(
    prefix='/youbot',
    tags=['YouBot']
)
@youbot_manage_router.post("/add")
async def add_youbot(youbot: SYoubotCurAdd = Depends()):
    youbot_id = await YoubotRepository.add_youbot(youbot)
    return{"ok": True, "youbot_id": youbot_id}

@youbot_manage_router.put("/update")
async def put_youbot(aruco_id, youbot: SYoubotCurAdd = Depends()):
    youbot = await YoubotRepository.update_youbot(youbot)
    return {**youbot}

@youbot_manage_router.get("/read")
async def get_all_youBots():
    youbots = await YoubotRepository.find_all_youbots()
    return {*youbots}
#@@@@@  YOUBOTS  @@@@@#


#@@@@@ VELOCITY  @@@@@#
youbot_velocity_router = APIRouter(
    prefix='/cmd_vel',
    tags=['Velocity']
)

@youbot_velocity_router.post("/")
async def add_cmd_vel(aruco_id, velocity: SVelocityTargetAdd = Depends()):
    return await YoubotVelocityRepository.add_velocity(aruco_id, velocity)

@youbot_velocity_router.put("/")
async def set_cmd_vel(aruco_id, velocity: SVelocityTargetAdd = Depends()):
    return await YoubotVelocityRepository.set_velocity(aruco_id, velocity)

@youbot_velocity_router.get("/")
async def get_cmd_vel(aruco_id = None):
    return {*await YoubotVelocityRepository.get_velocities_byAUID(aruco_id)}
#@@@@@ VELOCITY  @@@@@#