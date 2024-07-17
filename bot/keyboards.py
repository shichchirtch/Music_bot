from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)

pre_start_button = KeyboardButton(text='/start')

pre_start_clava = ReplyKeyboardMarkup(
    keyboard=[[pre_start_button]],
    resize_keyboard=True,
    input_field_placeholder='Приятного прослушивания'
)


ubiyci = InlineKeyboardButton(text=f'Убийцы', callback_data='Убийцы')
crystall = InlineKeyboardButton(text=f'Убийцы Crystal', callback_data='Crystal')
best = InlineKeyboardButton(text=f'The Best', callback_data='best')
start_inline_kb = InlineKeyboardMarkup(
            inline_keyboard= [[ubiyci],[crystall],[best]])

ubiyci_2013 = InlineKeyboardButton(text=f'2013 - Убийцы', callback_data='2013-U')
ubiyci_2014 = InlineKeyboardButton(text=f'2014 - Афина', callback_data='2014-U')
ubiyci_2014er = InlineKeyboardButton(text=f'2014 - Богиня[ер]', callback_data='2014-Uer')
ubiyci_2017 = InlineKeyboardButton(text=f'2017 - Гипноз', callback_data='2017-U')
ubiyci_2020 = InlineKeyboardButton(text=f'2020 - Даная', callback_data='2020-U')
ubiyci_2021 = InlineKeyboardButton(text=f'2021 - Твой светлый образ[ер]', callback_data='2021-U')
ubiyci_2022 = InlineKeyboardButton(text=f'2022 - Адвокат 2 [ер]', callback_data='2022-U')
albums_ubiyci_kb = InlineKeyboardMarkup(
            inline_keyboard= [[ubiyci_2013],[ubiyci_2014], [ubiyci_2014er], [ubiyci_2017],
                              [ubiyci_2020], [ubiyci_2021], [ubiyci_2022]])

###########################################################################################

crystal_2016 = InlineKeyboardButton(text=f'2016 - Гривачи', callback_data='2016-C')
crystal_2016_2 = InlineKeyboardButton(text=f'2016 - Сауна', callback_data='2016_2-C')
crystal_2020 = InlineKeyboardButton(text=f'2020 - Выход', callback_data='2020-C')
crystal_2021 = InlineKeyboardButton(text=f'2021 - Сериалы', callback_data='2021-С')
crystal_2022 = InlineKeyboardButton(text=f'2022 - Зодиак', callback_data='2022-С')
crystal_2022_2 = InlineKeyboardButton(text=f'2022 - Убийцы Crystal', callback_data='2022_2-С')
crystal_2024 = InlineKeyboardButton(text=f'2024 - Скачать', callback_data='2024-С')

albums_crystal_kb = InlineKeyboardMarkup(
            inline_keyboard= [[crystal_2016], [crystal_2016_2], [crystal_2020],
                              [crystal_2021], [crystal_2022], [crystal_2022_2], [crystal_2024]])
############################################################################################

# 1 album ubiyci
ubiyci_2013_1 = InlineKeyboardButton(text=f'1. Харе Кришна', callback_data='Харе Кришна')
ubiyci_2013_2 = InlineKeyboardButton(text=f'2. Селебы', callback_data='Селебы')
ubiyci_2013_3 = InlineKeyboardButton(text=f'3. Россия', callback_data='Россия')
ubiyci_2013_4 = InlineKeyboardButton(text=f'4. Что ? Где ? Когда ?', callback_data='Что')
ubiyci_2013_5 = InlineKeyboardButton(text=f'5. Лударь', callback_data='Лударь')
ubiyci_2013_6 = InlineKeyboardButton(text=f'6. Андрей', callback_data='Андрей')
ubiyci_2013_7 = InlineKeyboardButton(text=f'7. Tiger', callback_data='Tiger')
ubiyci_2013_back = InlineKeyboardButton(text=f'Назад к списку альбомов', callback_data='Назад')

album_ubiyci_kb_1 = InlineKeyboardMarkup(
            inline_keyboard= [[ubiyci_2013_1],[ubiyci_2013_2],[ubiyci_2013_3], [ubiyci_2013_4],
                              [ubiyci_2013_5], [ubiyci_2013_6], [ubiyci_2013_7],[ubiyci_2013_back]])

#########################################################################################

# 2 Album Ubiyci

ubiyci_2014_1 = InlineKeyboardButton(text=f'1. LGBT', callback_data='LGBT')
ubiyci_2014_2 = InlineKeyboardButton(text=f'2. 30 лет', callback_data='30 лет')
ubiyci_2014_3 = InlineKeyboardButton(text=f'3. Селебы', callback_data='Селебы2')
ubiyci_2014_4 = InlineKeyboardButton(text=f'4. Tiger', callback_data='Tiger2')
ubiyci_2014_5 = InlineKeyboardButton(text=f'5. Горжусь', callback_data='Горжусь')
ubiyci_2014_6 = InlineKeyboardButton(text=f'6. Драка из-за баб', callback_data='Драка')
ubiyci_2014_7 = InlineKeyboardButton(text=f'7. NLB', callback_data='NLB')

album_ubiyci_kb_2 = InlineKeyboardMarkup(
            inline_keyboard= [[ubiyci_2014_1],[ubiyci_2014_2],[ubiyci_2014_3], [ubiyci_2014_4],
                              [ubiyci_2014_5], [ubiyci_2014_6], [ubiyci_2014_7],[ubiyci_2013_back]])

###########################################################################################

# 3 Albuk Ubiyci
ubiyci_2014er_1 = InlineKeyboardButton(text=f'1. Цивил', callback_data='Цивил')
ubiyci_2014er_2 = InlineKeyboardButton(text=f'2. Два икса', callback_data='Два')
ubiyci_2014er_3 = InlineKeyboardButton(text=f'3. Конец', callback_data='Конец')

album_ubiyci_kb_3 = InlineKeyboardMarkup(
            inline_keyboard= [[ubiyci_2014er_1],[ubiyci_2014er_2],
                              [ubiyci_2014er_3],[ubiyci_2013_back]])
####################################################################################

#4 Album Ubiyci
ubiyci_2017_1 = InlineKeyboardButton(text=f'1. Гипноз', callback_data='Гипноз')
ubiyci_2017_2 = InlineKeyboardButton(text=f'2. Счёт', callback_data='Счёт')
ubiyci_2017_3 = InlineKeyboardButton(text=f'3. Динамо', callback_data='Динамо')
ubiyci_2017_4 = InlineKeyboardButton(text=f'4. Секретарша', callback_data='Секретарша')
ubiyci_2017_5 = InlineKeyboardButton(text=f'5. Имя твоё', callback_data='Имя')

album_ubiyci_kb_4 = InlineKeyboardMarkup(
            inline_keyboard= [[ubiyci_2017_1],[ubiyci_2017_2],
                              [ubiyci_2017_3],[ubiyci_2017_4], [ubiyci_2017_5],
                              [ubiyci_2013_back]])
###############################################################################

# 5 Album Ubiycy
ubiyci_2020_1 = InlineKeyboardButton(text=f'1. На ступеньку выше', callback_data='На ступеньку')
ubiyci_2020_2 = InlineKeyboardButton(text=f'2. Саларьево', callback_data='Саларьево')
ubiyci_2020_3 = InlineKeyboardButton(text=f'3. Ножики', callback_data='Ножики')
ubiyci_2020_4 = InlineKeyboardButton(text=f'4. В пододеяльнике', callback_data='В пододеяльнике')
ubiyci_2020_5 = InlineKeyboardButton(text=f'5. Шалость удалась', callback_data='Шалость')
ubiyci_2020_6 = InlineKeyboardButton(text=f'6. Не Виноваты', callback_data='Не Виноваты')
ubiyci_2020_7 = InlineKeyboardButton(text=f'7. Даная', callback_data='Даная')

album_ubiyci_kb_5 = InlineKeyboardMarkup(
            inline_keyboard= [[ubiyci_2020_1],[ubiyci_2020_2],[ubiyci_2020_3], [ubiyci_2020_4],
                              [ubiyci_2020_5],[ubiyci_2020_6], [ubiyci_2020_7],
                              [ubiyci_2013_back]])

############################################################################################

# 6 Albul Ubiyci

ubiyci_2021_1 = InlineKeyboardButton(text=f'1. В лесу', callback_data='В лесу')
ubiyci_2021_2 = InlineKeyboardButton(text=f'2. Следующая станция', callback_data='станция')
ubiyci_2021_3 = InlineKeyboardButton(text=f'3. Тошнота', callback_data='Тошнота')
ubiyci_2021_4 = InlineKeyboardButton(text=f'4. Бей по ногам', callback_data='Бей')

album_ubiyci_kb_6 = InlineKeyboardMarkup(
            inline_keyboard= [[ubiyci_2021_1],[ubiyci_2021_2],[ubiyci_2021_3], [ubiyci_2021_4],
                              [ubiyci_2013_back]])
###############################################################################################3

# 7 Album Ubiyci

ubiyci_2022_1 = InlineKeyboardButton(text=f'1. Антистресс', callback_data='Антистресс')
ubiyci_2022_2 = InlineKeyboardButton(text=f'2. Реку перейти', callback_data='реку')

album_ubiyci_kb_7 = InlineKeyboardMarkup(
            inline_keyboard= [[ubiyci_2022_1],[ubiyci_2022_2],
                              [ubiyci_2013_back]])
#################################################################################################
# 1 Album Crystal

crystal_2016_a1 = InlineKeyboardButton(text=f'Гривачи', callback_data='Гривачи')
crystal_2016_a2 = InlineKeyboardButton(text=f'Sport', callback_data='Sport')
crystal_2016_a3 = InlineKeyboardButton(text=f'Не буду спорить', callback_data='Не буду спорить')
crystal_2016_a4 = InlineKeyboardButton(text=f'Футбол', callback_data='Футбол')

album_crystal_kb_1 = InlineKeyboardMarkup(
            inline_keyboard= [[crystal_2016_a1],[crystal_2016_a2], [crystal_2016_a3], [crystal_2016_a4],
                              [ubiyci_2013_back]])

#################################################################################################

# 2 Album Crystal
crystal_2016_b1 = InlineKeyboardButton(text=f'1. Я', callback_data='Я')
crystal_2016_b2 = InlineKeyboardButton(text=f'2. Сауна', callback_data='Сауна')
crystal_2016_b3 = InlineKeyboardButton(text=f'3. Кришна', callback_data='Кришна')
crystal_2016_b4 = InlineKeyboardButton(text=f'4. Плакал', callback_data='Плакал')
crystal_2016_b5 = InlineKeyboardButton(text=f'5. Русалка', callback_data='Русалка')
crystal_2016_b6 = InlineKeyboardButton(text=f'6. Герой', callback_data='Герой')
crystal_2016_b7 = InlineKeyboardButton(text=f'7. Сьюзи', callback_data='Сьюзи')
album_crystal_kb_3 = InlineKeyboardMarkup(
            inline_keyboard= [[crystal_2016_b1],[crystal_2016_b2], [crystal_2016_b3],[crystal_2016_b4],
                              [crystal_2016_b5],[crystal_2016_b6],[crystal_2016_b7], [ubiyci_2013_back]])


#############################################################################################
# 3 Album Crystal

crystal_2020_1 = InlineKeyboardButton(text=f'1. Андрей', callback_data='Андрей')
crystal_2020_2 = InlineKeyboardButton(text=f'2. Ленина', callback_data='Ленина')
crystal_2020_3 = InlineKeyboardButton(text=f'3. Бескайфовая', callback_data='Бескайфовая')
crystal_2020_4 = InlineKeyboardButton(text=f'4. Андеграундный рай', callback_data='Андеграундный рай')
crystal_2020_5 = InlineKeyboardButton(text=f'5. Сон', callback_data='Сон')
crystal_2020_6 = InlineKeyboardButton(text=f'6. Бурятия', callback_data='Бурятия')
crystal_2020_7 = InlineKeyboardButton(text=f'7. Террористы', callback_data='Террористы')
crystal_2020_8 = InlineKeyboardButton(text=f'8. Вестник Грядущего Добра', callback_data='Вестник')
crystal_2020_9 = InlineKeyboardButton(text=f'9. Сама Сатана', callback_data='Сама')
album_crystal_kb_4 = InlineKeyboardMarkup(
            inline_keyboard= [[crystal_2020_1], [crystal_2020_2], [crystal_2020_3],
                              [crystal_2020_4], [crystal_2020_5], [crystal_2020_6], [crystal_2020_7],
                              [crystal_2020_8], [crystal_2020_9],[ubiyci_2013_back]])

###########################################################################################

# 4 Album Crystal

crystal_2021_1 = InlineKeyboardButton(text=f'1. Sailor Moon', callback_data='Sailor')
crystal_2021_2 = InlineKeyboardButton(text=f'2. Сериалы', callback_data='Сериалы')
crystal_2021_3 = InlineKeyboardButton(text=f'3. Герой remix', callback_data='Герой remix')

album_crystal_kb_5 = InlineKeyboardMarkup(
            inline_keyboard= [[crystal_2021_1], [crystal_2021_2], [crystal_2021_3],
                          [ubiyci_2013_back]])
################################################################################################

# 5 Album Crystal

crystal_2022_1 = InlineKeyboardButton(text=f'1. Новое Культурное Течение', callback_data='Течение')
crystal_2022_2 = InlineKeyboardButton(text=f'2. Пара Миллионов', callback_data='Пара')
crystal_2022_3 = InlineKeyboardButton(text=f'3. Nasty Настя', callback_data='Настя')
crystal_2022_4 = InlineKeyboardButton(text=f'4. Грибы', callback_data='Грибы')
crystal_2022_5 = InlineKeyboardButton(text=f'5. Корова', callback_data='Корова')
album_crystal_kb_6 = InlineKeyboardMarkup(
            inline_keyboard= [[crystal_2022_1], [crystal_2022_2], [crystal_2022_3],
                          [crystal_2022_4], [crystal_2022_5],[ubiyci_2013_back]])

####################################################################################################

# 6 Album
crystal_2022a_1 = InlineKeyboardButton(text=f'Без Названия', callback_data='Без Названия')
crystal_2022a_2 = InlineKeyboardButton(text=f'Гробы', callback_data='Гробы')
crystal_2022a_3 = InlineKeyboardButton(text=f'Модная Одежда', callback_data='одежда')
crystal_2022a_4 = InlineKeyboardButton(text=f'Насекомыми', callback_data='Насекомыми')
crystal_2022a_5 = InlineKeyboardButton(text=f'Танцы и музыка', callback_data='Танцы')
crystal_2022a_6 = InlineKeyboardButton(text=f'Лучшие мои друзья', callback_data='лучшие')
crystal_2022a_7 = InlineKeyboardButton(text=f'Я все вижу', callback_data='вижу')
crystal_2022a_8 = InlineKeyboardButton(text=f'В машине', callback_data='машине')

album_crystal_kb_7 = InlineKeyboardMarkup(
            inline_keyboard= [[crystal_2022a_1], [crystal_2022a_2], [crystal_2022a_3],
                          [crystal_2022a_4], [crystal_2022a_5], [crystal_2022a_6],
                              [crystal_2022a_7],[crystal_2022a_8],[ubiyci_2013_back]])


####################################################################################################

# 7 Album  Cryst
crystal_2024_1 = InlineKeyboardButton(text=f'Воскресенье', callback_data='Воскресенье')
crystal_2024_2 = InlineKeyboardButton(text=f'Dumb and Damber', callback_data='Dumb')
crystal_2024_3 = InlineKeyboardButton(text=f'Дикость', callback_data='дикость')
crystal_2024_4 = InlineKeyboardButton(text=f'Скачать', callback_data='Скачать')
crystal_2024_5 = InlineKeyboardButton(text=f'Жертва', callback_data='Жертва')


album_crystal_kb_8 = InlineKeyboardMarkup(
            inline_keyboard= [[crystal_2024_1], [crystal_2024_2], [crystal_2024_3],
                          [crystal_2024_4], [crystal_2024_5], [ubiyci_2013_back]])

















