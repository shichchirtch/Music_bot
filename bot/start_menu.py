from aiogram.types import BotCommand

async def set_main_menu(bot):

    main_menu_commands = [
        BotCommand(command='/back',
                   description='Kommen zurück zum menu'),

        BotCommand(command='/help',
                   description='Bot commands')]

    await bot.set_my_commands(main_menu_commands)

