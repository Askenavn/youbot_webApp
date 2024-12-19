from typing import Union
from pydantic import BaseModel, ConfigDict


class SYoubotCurAdd(BaseModel):
    aruco_id: Union[int, None] = 1
    arm_count: Union[int, None] = 1
    status: Union[str, None] = 'undefine'

class SYoubotCur(SYoubotCurAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SYoubotTargetAdd(BaseModel):
    aruco_id: Union[int, None] = 1
    x: Union[float, None] = 0.0
    y: Union[float, None] = 0.0
    z: Union[float, None] = 0.0
    w: Union[float, None] = 0.0

class SYoubotTarget(SYoubotTargetAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SVelocityTargetAdd(BaseModel):
    aruco_id: Union[int, None] = 1
    x: Union[float, None] = 0.0
    y: Union[float, None] = 0.0
    theta: Union[float, None] = 0.0

class SVelocityTarget(SVelocityTargetAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SFigureAdd(BaseModel):
    aruco_id: Union[int, None] = 1
    name: Union[str, None] = None
    r: Union[float, None] = 0.0
    k: Union[float, None] = 0.0

class SFigure(SFigureAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)



