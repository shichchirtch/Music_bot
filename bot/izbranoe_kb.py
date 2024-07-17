from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup
ub_best = InlineKeyboardButton(text=f'Убийцы', callback_data='UB')
cr_best = InlineKeyboardButton(text=f'Crystal', callback_data='CRY')
best_kb = InlineKeyboardMarkup(
            inline_keyboard= [[ub_best], [cr_best]])


izb_1 = InlineKeyboardButton(text=f'Кришна', callback_data='Кришна')
izb_2 = InlineKeyboardButton(text=f'Русалка', callback_data='Русалка')
izb_3 = InlineKeyboardButton(text=f'Ленина', callback_data='Ленина')
izb_4 = InlineKeyboardButton(text=f'Андеграундный рай', callback_data='Андеграундный рай')
izb_5 = InlineKeyboardButton(text=f'Бурятия', callback_data='Бурятия')
izb_6 = InlineKeyboardButton(text=f'Без Названия', callback_data='Без Названия')
izb_7 = InlineKeyboardButton(text=f'Лучшие мои друзья', callback_data='лучшие')
izb_8 = InlineKeyboardButton(text=f'Я все вижу', callback_data='вижу')
izb_9 = InlineKeyboardButton(text=f'Пинг-Понг', callback_data='Пинг-Понг')
izb_10 = InlineKeyboardButton(text=f'LGBT', callback_data='LGBT2')
back = InlineKeyboardButton(text=f'Назад в избранное', callback_data='Назад')

cr_best_list_kb  = InlineKeyboardMarkup(
            inline_keyboard= [[izb_1], [izb_2], [izb_3],[izb_4],[izb_5],[izb_6],[izb_7],
                              [izb_8],[izb_9],[izb_10],[back]])


iz_1 = InlineKeyboardButton(text=f'Селебы', callback_data='Селебы')
iz_2 = InlineKeyboardButton(text=f'Горжусь', callback_data='Горжусь')
iz_3 = InlineKeyboardButton(text=f'Цивил', callback_data='Цивил')
iz_4 = InlineKeyboardButton(text=f'Шалость удалась', callback_data='Шалость')
iz_5= InlineKeyboardButton(text=f'В лесу', callback_data='В лесу')
iz_6 = InlineKeyboardButton(text=f'Реку перейти', callback_data='реку')
ub_best_list_kb  = InlineKeyboardMarkup(
            inline_keyboard= [[iz_1], [iz_2], [iz_3],[iz_4],[iz_5],[iz_6],[back]])