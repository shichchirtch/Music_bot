from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis
from config import settings

using_redis = Redis(host=settings.REDIS_HOST)
redis_storage = RedisStorage(redis=using_redis)

# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSM_ST(StatesGroup):
    start = State()
    ubiyci = State()
    crystal = State()
    best = State()
    wait = State()
