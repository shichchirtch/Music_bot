from aiogram import Dispatcher
import asyncio
from command_handlers import ch_router
from inline_handlers import cb_router
from start_menu import set_main_menu
from FSM_states import redis_storage
from bot_instance import bot
from bot_base import init_models

async def main():
    await init_models()

    dp = Dispatcher(storage=redis_storage)
    dp.startup.register(set_main_menu)
    await set_main_menu(bot)
    dp.include_router(ch_router)
    dp.include_router(cb_router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
