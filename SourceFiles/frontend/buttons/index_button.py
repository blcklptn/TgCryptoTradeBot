from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def generate_enter_code_word():
    buttons = [
        [
            InlineKeyboardButton(text='Установить кодовое слово', callback_data='install_code_word')
        ],
        [
            InlineKeyboardButton(text='<< Назад', callback_data='my_cabinet'),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def generate_full_stat_button():
    buttons = [
        [
            InlineKeyboardButton(text='Краткая статистика', callback_data='my_cabinet'),
        ],
        [
            InlineKeyboardButton(text='Кодовое слово', callback_data='enter_code_word'),
        ],
        [
            InlineKeyboardButton(text='История обменов', callback_data='trade_history'),
        ],
        [
            InlineKeyboardButton(text='Ввести промокод', callback_data='enter_promo'),
        ],
        [
            InlineKeyboardButton(text='<< Назад', callback_data='back_to_main'),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def generate_my_cabinet_button():
    buttons = [
        [
            InlineKeyboardButton(text='Подробная статистика', callback_data='full_stat'),
        ],
        [
            InlineKeyboardButton(text='Кодовое слово', callback_data='enter_code_word'),
        ],
        [
            InlineKeyboardButton(text='История обменов', callback_data='trade_history'),
        ],
        [
            InlineKeyboardButton(text='Ввести промокод', callback_data='enter_promo'),
        ],
        [
            InlineKeyboardButton(text='<< Назад', callback_data='back_to_main'),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def generate_converter_button():
    button = [
        [
            InlineKeyboardButton(text='<< Назад', callback_data='coshelek'),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard

def generate_coshelek_button():
    buttons = [
        [
            InlineKeyboardButton(text='Рубль', callback_data='coshel_ruble'),
            InlineKeyboardButton(text='Bitcoin', callback_data='coshel_bitcoin'),
        ],
        [
            InlineKeyboardButton(text='Litecoin', callback_data='coshel_litecoin'),
        ],
        [
            InlineKeyboardButton(text='Ввести ваучер', callback_data='enter_vaucher'),
        ],
        [
            InlineKeyboardButton(text='Конвертер валют', callback_data='converter'),
        ],
        [
            InlineKeyboardButton(text='<< Назад', callback_data='back_to_main'),
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def generate_must_lucky_button():
    button = [
        [
            InlineKeyboardButton(text='<< Назад', callback_data='lottery'),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard

def generate_info_button():
    buttons = [
        [
            InlineKeyboardButton(text='🔄 Обмен', callback_data='trade_info'),
            InlineKeyboardButton(text='💰 Баланс', callback_data='balance_info'),
        ],
        [
            InlineKeyboardButton(text='🗄 Мой кабинет', callback_data='cabinet_info'),
        ],
        [
            InlineKeyboardButton(text='<< Назад', callback_data='back_to_main'),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def generate_to_info_button():
    button = [
        [
            InlineKeyboardButton(text='<< Назад', callback_data='info'),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard

def generate_lottery_button():
    buttons = [
        [
            InlineKeyboardButton(text='Самый везучий 1.000р', callback_data='must_lucky')
        ],
        [
            InlineKeyboardButton(text='<< Назад', callback_data='to_main'),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def generate_index_button():
    buttons = [
        [
            InlineKeyboardButton(text='↙️ Купить', callback_data='buy'),
            InlineKeyboardButton(text='↗️ Продать', callback_data='sell'),
        ],
        [
            InlineKeyboardButton(text='👛 Кошелек', callback_data='coshelek'),
            InlineKeyboardButton(text='👥 Рефералка', callback_data='referral')
        ],
        [
            InlineKeyboardButton(text='🎰 Лотерея', callback_data='lottery'),
            InlineKeyboardButton(text='🗄 Мой кабинет', callback_data='my_cabinet'),
        ],
        [
            InlineKeyboardButton(text='🤑 Миксер', url='https://t.me/ab_chat'),
        ],
        [
            InlineKeyboardButton(text='💬 Чат', url='https://t.me/ab_chat'),
            InlineKeyboardButton(text='📢 Канал', url='https://t.me/mudak'),
        ],
        [
            InlineKeyboardButton(text='📑 Отзывы', url='https://t.me/mudak'),
            InlineKeyboardButton(text='🆘 Оператор', url='https://t.me/blcklptn'),
        ],
        [
            InlineKeyboardButton(text='ℹ️ Инфо', callback_data='info'),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard