from aiogram.types import CallbackQuery, Message
from aiogram.filters import BaseFilter
from postgres_functions import check_user_in_table



class PRE_START(BaseFilter):
    async def __call__(self, message: Message):
        data = await check_user_in_table(message.from_user.id)
        if data:
            return False
        return True


class START_UB_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'Убийцы':
            return True
        return False


class START_CR_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'Crystal':
            return True
        return False


class START_BEST_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'best':
            return True
        return False


class START_UB_1_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data in ('2013-U', '2014-U', '2014-Uer', '2017-U', '2020-U', '2021-U', '2022-U'):
            return True
        return False


class UB_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data in ('Харе Кришна', 'Селебы', 'Россия', 'Что', 'Лударь', 'Андрей', 'Tiger', 'Назад',
                             'LGBT', '30 лет', 'Селебы2', 'Tiger2', 'Горжусь', 'Драка', 'NLB',
                             'Цивил', 'Два', 'Конец', 'Гипноз', 'Счёт', 'Динамо', 'Секретарша', 'Имя',
                             'На ступеньку', 'Саларьево', 'Ножики', 'В пододеяльнике', 'Шалость',
                             'Не Виноваты', 'Даная', 'В лесу', 'станция', 'Тошнота', 'Бей', 'Антистресс', 'реку'
                             ):
            return True
        return False


class START_CRY_1_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data in ('2016-C', '2016_2-C', '2020-C', '2021-С', '2022-С', '2022_2-С', '2024-С'):
            return True
        return False


class CRY_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data in ('Гривачи', 'Sport', 'Не буду спорить', 'Футбол', 'Кришна',
                             'Сауна', 'Я', 'Плакал', 'Русалка', 'Герой', 'Сьюзи', 'Андрей', 'Ленина', 'Бескайфовая',
                             'Андеграундный рай', 'Сон', 'Бурятия', 'Террористы', 'Вестник',
                             'Сама', 'Sailor', 'Сериалы', 'Герой remix', 'Течение', 'Пара',
                             'Настя', 'Грибы', 'Корова', 'Без Названия', 'Гробы', 'одежда',
                             'Насекомыми', 'Танцы', 'лучшие', 'вижу', 'машине', 'Воскресенье',
                             'Dumb', 'дикость', 'Скачать', 'Жертва', 'Назад'
                             ):
            return True
        return False

class START_BEST_1_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data in ('UB', 'CRY'):
            return True
        return False

class BEST_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data in ( 'Назад', 'Кришна', 'Русалка', 'Ленина', 'Бурятия', 'Без Названия',
                              'лучшие', 'вижу', 'Воскресенье', 'Селебы', 'Горжусь', 'Цивил',
                              'Шалость', 'В лесу', 'LGBT2', 'реку', 'Андеграундный рай','Пинг-Понг'
                             ):
            return True
        return False