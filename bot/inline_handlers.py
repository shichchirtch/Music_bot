from aiogram import Router
from filters import *
import asyncio
from pagination import *
from aiogram.types import CallbackQuery, Message, InputMediaPhoto
from aiogram.exceptions import TelegramBadRequest
from keyboards import *
from postgres_functions import *
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from izbranoe_kb import *
from bot_instance import bot
import json
from FSM_states import FSM_ST

cb_router = Router()


@cb_router.callback_query(StateFilter(FSM_ST.start), START_UB_FILTER())
async def go_to_ubiyci(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSM_ST.ubiyci)
    user_id = callback.from_user.id
    try:
        att = await callback.message.edit_media(
            media=InputMediaPhoto(
                media=ubiycy_foto),
            reply_markup=albums_ubiyci_kb)
        data = await return_kadr(user_id)
        if data != '':
            json_att = att.model_dump_json(exclude_none=True)
            await insert_data_in_kadr(user_id, json_att)

    except TelegramBadRequest:
        print('go to ubiyci into Exeption')
    await callback.answer()


@cb_router.callback_query(StateFilter(FSM_ST.start), START_CR_FILTER())
async def go_to_crystal(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSM_ST.crystal)
    user_id = callback.from_user.id
    try:
        att = await callback.message.edit_media(
            media=InputMediaPhoto(
                media=cristal_foto),
            reply_markup=albums_crystal_kb)
        data = await return_kadr(user_id)
        if data != '':
            json_att = att.model_dump_json(exclude_none=True)
            await insert_data_in_kadr(user_id, json_att)

    except TelegramBadRequest:
        print('go to crystal into Exeption')
    await callback.answer()


@cb_router.callback_query(StateFilter(FSM_ST.start), START_BEST_FILTER())
async def go_to_best(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSM_ST.best)
    user_id = callback.from_user.id
    try:
        att = await callback.message.edit_media(
            media=InputMediaPhoto(
                media=best_foto),
            reply_markup=best_kb)
        data = await return_kadr(user_id)
        if data != '':
            json_att = att.model_dump_json(exclude_none=True)
            await insert_data_in_kadr(user_id, json_att)

    except TelegramBadRequest:
        print('go to best into Exeption')
    await callback.answer()


@cb_router.callback_query(StateFilter(FSM_ST.ubiyci), START_UB_1_FILTER())
async def go_to_ub_1(callback: CallbackQuery):
    print('callback.data = ', callback.data)
    user_id = callback.from_user.id
    callback_data_dict = {'2013-U': (album_ubiyci_kb_1, ub_1), '2014-U': (album_ubiyci_kb_2, ub_2),
                          '2014-Uer': (album_ubiyci_kb_3, ub_3), '2017-U': (album_ubiyci_kb_4, ub_4),
                          '2020-U': (album_ubiyci_kb_5, ub_5), '2021-U': (album_ubiyci_kb_6, ub_6),
                          '2022-U': (album_ubiyci_kb_7, ub_7)
                          }
    try:
        att = await callback.message.edit_media(
            media=InputMediaPhoto(
                media=callback_data_dict[callback.data][1]),
            reply_markup=callback_data_dict[callback.data][0])
        data = await return_kadr(user_id)
        if data != '':
            json_att = att.model_dump_json(exclude_none=True)
            await insert_data_in_kadr(user_id, json_att)

    except TelegramBadRequest:
        print('go to best into Exeption')
    await callback.answer()


@cb_router.callback_query(StateFilter(FSM_ST.ubiyci), UB_FILTER(), ~StateFilter(FSM_ST.wait))
async def go_INTO_ub(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    song = callback.data
    if song != 'Назад':
        previous_song = await return_song(user_id)
        if song == previous_song:
            await state.set_state(FSM_ST.wait)
            await asyncio.sleep(20)
            await state.set_state(FSM_ST.ubiyci)
        await callback.message.answer_audio(sound_ub_dict[song])
        await insert_data_in_song(user_id, song)
    else:
        ubiyci_foto_atw = await callback.message.answer_photo(ubiycy_foto,
                                                              reply_markup=albums_ubiyci_kb)

        del_data = await return_kadr(user_id)
        return_to_message = Message(**json.loads(del_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        json_att = ubiyci_foto_atw.model_dump_json(exclude_none=True)
        await insert_data_in_kadr(user_id, json_att)


@cb_router.callback_query(StateFilter(FSM_ST.crystal), START_CRY_1_FILTER())
async def go_to_crystal_albums(callback: CallbackQuery, ):
    print('callback.data = ', callback.data)
    user_id = callback.from_user.id
    callback_data_cry_dict = {'2016-C': (album_crystal_kb_1, cr_1),
                              '2016_2-C': (album_crystal_kb_3, cr_3), '2020-C': (album_crystal_kb_4, cr_4),
                              '2021-С': (album_crystal_kb_5, cr_5), '2022-С': (album_crystal_kb_6, cr_6),
                              '2022_2-С': (album_crystal_kb_7, cr_7), '2024-С': (album_crystal_kb_8, cr_8)
                              }

    try:
        att = await callback.message.edit_media(
            media=InputMediaPhoto(
                media=callback_data_cry_dict[callback.data][1]),
            reply_markup=callback_data_cry_dict[callback.data][0])
        data = await return_kadr(user_id)
        if data != '':
            json_att = att.model_dump_json(exclude_none=True)
            await insert_data_in_kadr(user_id, json_att)

    except TelegramBadRequest:
        print('go to best into Exeption')
    await callback.answer()


@cb_router.callback_query(StateFilter(FSM_ST.crystal), CRY_FILTER(), ~StateFilter(FSM_ST.wait))
async def go_INTO_cry(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    song = callback.data
    if song != 'Назад':
        previous_song = await return_song(user_id)
        if song == previous_song:
            await state.set_state(FSM_ST.wait)
            await asyncio.sleep(20)
            await state.set_state(FSM_ST.crystal)
        await callback.message.answer_audio(sound_cry_dict[song])
        await insert_data_in_song(user_id, song)
    else:
        ubiyci_foto_atw = await callback.message.answer_photo(cristal_foto,
                                                              reply_markup=albums_crystal_kb)

        del_data = await return_kadr(user_id)
        return_to_message = Message(**json.loads(del_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        json_att = ubiyci_foto_atw.model_dump_json(exclude_none=True)
        await insert_data_in_kadr(user_id, json_att)


@cb_router.callback_query(StateFilter(FSM_ST.best), START_BEST_1_FILTER())
async def go_to_best(callback: CallbackQuery, ):
    print('callback.data = ', callback.data)
    user_id = callback.from_user.id
    callback_data_best_dict = {'UB': (ub_best_list_kb, lexa),
                               'CRY': (cr_best_list_kb, vika)}
    try:
        att = await callback.message.edit_media(
            media=InputMediaPhoto(
                media=callback_data_best_dict[callback.data][1]),
            reply_markup=callback_data_best_dict[callback.data][0])
        data = await return_kadr(user_id)
        if data != '':
            json_att = att.model_dump_json(exclude_none=True)
            await insert_data_in_kadr(user_id, json_att)

    except TelegramBadRequest:
        print('go to best into Exeption')
    await callback.answer()


@cb_router.callback_query(StateFilter(FSM_ST.best), BEST_FILTER(), ~StateFilter(FSM_ST.wait))
async def go_INTO_best(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    song = callback.data
    print('song = ', song)
    if song != 'Назад':
        previous_song = await return_song(user_id)
        if song == previous_song:
            await state.set_state(FSM_ST.wait)
            await asyncio.sleep(200)
            await state.set_state(FSM_ST.best)
        await callback.message.answer_audio(izb_dict[song])
        await insert_data_in_song(user_id, song)
    else:
        ubiyci_foto_atw = await callback.message.answer_photo(best_foto,
                                                              reply_markup=best_kb)

        del_data = await return_kadr(user_id)
        return_to_message = Message(**json.loads(del_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        json_att = ubiyci_foto_atw.model_dump_json(exclude_none=True)
        await insert_data_in_kadr(user_id, json_att)
