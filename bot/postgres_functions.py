from bot_base import session_marker, User
from sqlalchemy import select

async def insert_new_user_in_table(user_tg_id: int, name: str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        if not needed_data:
            print('Now we are into first function')
            new_us = User(tg_us_id=user_tg_id, user_name=name)
            session.add(new_us)
            await session.commit()

async def check_user_in_table(user_tg_id:int):
    """Функция проверяет есть ли юзер в БД"""
    async with session_marker() as session:
        print("Work check_user Function")
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        data = query.one_or_none()
        return data

async def insert_data_in_kadr(user_id:int, kadr_data:str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        needed_data.kadr = kadr_data
        await session.commit()
# Переписать значение в БД
async def insert_data_in_song(user_id:int, song:str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        needed_data.song = song
        await session.commit()
# Вернуть данные из бд
async def return_song(user_id):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        song = needed_data.song
        return song
# Откатить значение колонки к стартовому
async def reset_song(user_id):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        needed_data.song = 'not_repeat'
        await session.commit()

async def return_kadr(user_id):
    async with session_marker() as session:
        print("Works return_kadr Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        kadr_msg = needed_data.kadr
        return kadr_msg


async def insert_data_in_help(user_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        needed_data.help = 'Help'
        await session.commit()


async def return_help(user_id):
    async with session_marker() as session:
        print("Works return_kadr Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        help = needed_data.help
        return help


async def reset_help(user_id):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        needed_data.help = ''
        await session.commit()






