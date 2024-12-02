from aiogram import Router, F
import asyncio
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from postgres_functions import *
from pagination import start_foto
from keyboards import pre_start_clava, start_inline_kb
from aiogram.fsm.context import FSMContext
import json
from bot_instance import bot
from filters import PRE_START
from lexicon import *
from FSM_states import FSM_ST

ch_router = Router()

@ch_router.message(~F.text)
async def delete_not_text_type_messages(message: Message):
    await message.delete()


@ch_router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    data = await check_user_in_table(user_id)
    if not data:
        print("))))))))))))))))")
        await state.set_state(FSM_ST.start)
        await insert_new_user_in_table(user_id, user_name)
        first_foto_atw = await message.answer_photo(start_foto,
                                                    reply_markup=start_inline_kb)
        json_att = first_foto_atw.model_dump_json(exclude_none=True)
        await insert_data_in_kadr(user_id, json_att)
    else:
        await message.delete()


@ch_router.message(PRE_START())
async def before_start(message: Message):
    prestart_ant = await message.answer(text='Нажми на кнопку <b>start</b> !',
                                        reply_markup=pre_start_clava)
    await message.delete()
    await asyncio.sleep(3)
    await prestart_ant.delete()


@ch_router.message(Command('help'))
async def process_help_command(message: Message):
    # current_state = await state.get_state()
    user_id = message.from_user.id
    if not await return_help(user_id):
        await insert_data_in_help(user_id)
        att = await message.answer(text=help_text)
        await asyncio.sleep(22)
        await message.delete()
        await att.delete()
        await reset_help(user_id)
    else:
        await message.delete()
    # await state.set_state(current_state)


@ch_router.message(Command('back'))
async def process_back_command(message: Message, state: FSMContext):
    print('INTO Back')
    await state.set_state(FSM_ST.start)
    user_id = message.from_user.id
    # data = await return_kadr(user_id)
    # if data != '':
    #     return_to_message = Message(**json.loads(data))
    #     msg = Message.model_validate(return_to_message).as_(bot)
    #     await message.delete()
    #     await msg.delete()
    first_foto_atw = await message.answer_photo(start_foto,
                                                reply_markup=start_inline_kb)
    js_first_foto_atw = first_foto_atw.model_dump_json(exclude_none=True)
    await insert_data_in_kadr(user_id, js_first_foto_atw)


@ch_router.message()
async def delete_text_messages(message: Message):
    print('Works this shame handler')
    await message.delete()
