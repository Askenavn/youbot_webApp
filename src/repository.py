from sqlalchemy import select, update, desc
from database import new_session, YoubotTargetOrm, YoubotOrm, YoubotVelocityORM, TargetFigureORM
from schemas import SYoubotCurAdd, SYoubotTargetAdd, SVelocityTargetAdd, SFigureAdd

fig_names = ('circle', 'spiral', 'deltoid', 'spiral_diff', 'circle_diff')


class YoubotTargetRepository:
    @classmethod
    async def add_target(cls, target: SYoubotTargetAdd):
        async with new_session() as session:
            target_dict = target.model_dump()

            target = YoubotTargetOrm(**target_dict)
            session.add(target)
            await session.flush()
            await session.commit()
            return target.id
                     
    @classmethod
    async def find_target(cls, aruco_id: int):
        async with new_session() as session:
            query = select(YoubotTargetOrm).order_by(YoubotTargetOrm.id).filter(YoubotTargetOrm.aruco_id == aruco_id)
            result = await session.execute(query)
            target_models = result.scalars().all()
            return target_models
        
    @classmethod
    async def find_all_targets(cls):
        async with new_session() as session:
            query = select(YoubotTargetOrm).order_by(desc(YoubotTargetOrm.aruco_id))
            result = await session.execute(query)
            target_models = result.scalars().all()
            return target_models
        
    @classmethod
    async def add_figure(cls, au_id, fig: SFigureAdd):
        async with new_session() as session:
            if await session.get(TargetFigureORM, au_id) is None:
                fig_dict = fig.model_dump()
                fig = TargetFigureORM(**fig_dict)
                if fig.name in fig_names:
                    session.add(fig)
                    await session.flush()
                    await session.commit()
                    return {"ok": True}
                else:
                    return {'ok': False, 'msg': 'No fig name matched'}
            else:
                return {'ok': False, 'msg': 'Already exsists'}
                    
    @classmethod
    async def set_new_figure(cls, au_id, fig: SFigureAdd):
        async with new_session() as session:
            try:
                if fig.name in fig_names:
                    query = (update(TargetFigureORM).
                            where(TargetFigureORM.aruco_id == au_id).
                            values(name = fig.name))
                    await session.execute(query)
                    await session.flush()
                    await session.commit()
                    return {'ok': True}
                else:
                    session.rollback()
                    return {'ok': False, 'msg': 'No fig name matched'}
            except:
                session.rollback()
                return {'ok': False}
            
    @classmethod
    async def get_figures(cls, id = None):
        try:
            async with new_session() as session:
                query = select(TargetFigureORM).order_by(TargetFigureORM.aruco_id)
                if id is not None:
                    query = query.where(TargetFigureORM.aruco_id == id)
                result = await session.execute(query)
                return result.scalars().all()
        except:
            raise 

            


class YoubotRepository:             
    @classmethod
    async def add_youbot(cls, youbot: SYoubotCurAdd):
        async with new_session() as session:
            youbot_dict = youbot.model_dump()
            youbot = YoubotOrm(**youbot_dict)
            session.add(youbot)
            await session.flush()
            await session.commit()
            return youbot.id
                
    @classmethod
    async def update_youbot(cls, youbot: SYoubotCurAdd):
        async with new_session() as session:
            youbot_old = await session.get(YoubotOrm, youbot.aruco_id)
            if youbot_old:
                try:
                    youbot_old.arm_count = youbot.arm_count
                    await session.flush()
                    await session.commit()
                    return {"ok": True}
                except:
                    session.rollback()
            return {"ok": False}


        async with new_session() as session:
            query = select(YoubotOrm).order_by(YoubotOrm.id).filter(YoubotOrm.aruco_id == youbot.aruco_id)
            result = await session.execute(query)
            youbot = result.scalars().all()
            return youbot

    @classmethod
    async def find_all_youbots(cls):
        async with new_session() as session:
            query = select(YoubotOrm).order_by(YoubotOrm.id)
            result = await session.execute(query)
            youbots_models = result.scalars().all()
            return youbots_models
        
    @classmethod
    async def find_youbot(cls, aruco_id: int):
        async with new_session() as session:
            query = select(YoubotOrm).order_by(YoubotOrm.id).filter(YoubotOrm.aruco_id == aruco_id)
            result = await session.execute(query)
            youbot = result.scalars().all()
            return youbot


class YoubotVelocityRepository:
    @classmethod
    async def add_velocity(cls, au_id, velocity: SVelocityTargetAdd):
        async with new_session() as session:
            if await session.get(YoubotVelocityORM, au_id) is None:
                vel_dic = velocity.model_dump()
                vel = YoubotVelocityORM(**vel_dic)
                session.add(vel)
                await session.flush()
                await session.commit()
                return {"ok": True}
            else:
                return {'ok': False, 'msg': 'Already exsist'}

    @classmethod
    async def set_velocity(cls, au_id, velocity: SVelocityTargetAdd):
        async with new_session() as session:
            try:
                query = (update(YoubotVelocityORM).
                         where(YoubotVelocityORM.aruco_id == au_id).
                         values(x = velocity.x, y = velocity.y, theta = velocity.theta))
                await session.execute(query)
                await session.flush()
                await session.commit()
                return {'ok': True}
            except:
                session.rollback()
                return {'ok': False}

    @classmethod
    async def get_velocities_byAUID(cls, id = None):
        try:
            async with new_session() as session:
                query = select(YoubotVelocityORM).order_by(YoubotVelocityORM.aruco_id)
                if id is not None:
                    query = query.where(YoubotVelocityORM.aruco_id == id)
                result = await session.execute(query)
                return result.scalars().all()
        except:
            raise 
