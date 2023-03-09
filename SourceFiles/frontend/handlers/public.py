from aiogram import Router
from aiogram.types import Message, CallbackQuery
from frontend.message import index_message, info_message, trade_info, balance_info, cabinet_info, \
                             replyes_message, generate_coshelek, lottery_message, must_lucky_message, \
                             converter_message, my_cabinet_message, full_stat_message, code_word_message
from frontend.buttons import index_button
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from middleware import crud

router = Router()

# index menu control
@router.message(commands=['start'])
async def index(message: Message):
    await message.answer(index_message.data, reply_markup=index_button.generate_index_button(), parse_mode='HTML')

@router.callback_query(text ='info')
async def info_call(callback: CallbackQuery):
    await go_to_info(callback.message)

@router.callback_query(text='back_to_main')
async def info_back_to_main(callback: CallbackQuery):
    await go_to_main(callback.message)

@router.callback_query(text='trade_info')
async def info_traid_call(callback: CallbackQuery):
    await go_to_trade_info(callback.message)

@router.callback_query(text='balance_info')
async def info_balance_call(callback: CallbackQuery):
    await go_to_balance_info(callback.message)

@router.callback_query(text='cabinet_info')
async def info_cabinet_call(callback: CallbackQuery):
    await go_to_cabinet_info(callback.message)

@router.callback_query(text='coshelek')
async def coshelek_call(callback: CallbackQuery):
    await go_to_coshelek(callback.message)

@router.callback_query(text='lottery')
async def lottery_call(callback: CallbackQuery):
    await go_to_lottery(callback.message)

@router.callback_query(text='to_main')
async def to_main_call(callback: CallbackQuery):
    await go_to_main(callback.message)

@router.callback_query(text='must_lucky')
async def must_lucky_call(callback: CallbackQuery):
    await go_to_must_lucky(callback.message)

@router.callback_query(text='converter')
async def converter_call(callback: CallbackQuery):
    await go_to_converter(callback.message)

@router.callback_query(text='my_cabinet')
async def my_cabinet_call(callback: CallbackQuery):
    await go_to_my_cabinet(callback.message)

@router.callback_query(text='full_stat')
async def full_stat_call(callback: CallbackQuery):
    await go_to_full_stat(callback.message)

@router.callback_query(text='enter_code_word')
async def enter_code_word_call(callback: CallbackQuery):
    await go_to_enter_code_word(callback.message)

@router.callback_query(text='BTC_LTC')
async def BTC_LTC(callback: CallbackQuery):
    await go_to_BTC_LTC(callback.message)

@router.callback_query(text='managment')
async def managment(callback: CallbackQuery):
    await go_to_managment(callback.message)

@router.callback_query(text='balance_CB')
async def check_balance_CB(callback: CallbackQuery):
    await go_to_balance_CB(callback.message)

@router.callback_query(text='balance')
async def check_balance(callback: CallbackQuery):
    await go_to_balance(callback.message)

@router.callback_query(text='ADMIN_MENU')
async def ADMIN_MENU(callback: CallbackQuery):
    await go_to_ADMIN_MENU(callback.message)


# -------- Callbacks
async def go_to_enter_code_word(message: Message):
    await message.edit_text(code_word_message.generate_data(), reply_markup=index_button.generate_enter_code_word(), parse_mode='HTML')

async def go_to_full_stat(message: Message):
    await message.edit_text(full_stat_message.generate_full_stat_message(),reply_markup=index_button.generate_full_stat_button(), parse_mode='HTML' )

async def go_to_my_cabinet(message: Message):
    await message.edit_text(my_cabinet_message.data, reply_markup=index_button.generate_my_cabinet_button(), parse_mode='HTML')

async def go_to_converter(message: Message):
    await message.edit_text(converter_message.data, reply_markup=index_button.generate_converter_button(), parse_mode='HTML')

async def go_to_must_lucky(message: Message):
    await message.edit_text(must_lucky_message.data, reply_markup=index_button.generate_must_lucky_button(), parse_mode='HTML')

async def go_to_main(message: Message):
    await message.edit_text(index_message.data, reply_markup=index_button.generate_index_button(), parse_mode='HTML')

async def go_to_lottery(message: Message):
    await message.edit_text(lottery_message.data, reply_markup=index_button.generate_lottery_button(), parse_mode='HTML')

async def go_to_coshelek(message: Message):
    coshel = generate_coshelek.generate_coshelek()
    await message.edit_text(coshel, reply_markup=index_button.generate_coshelek_button(), parse_mode='HTML')

async def go_to_cabinet_info(message: Message):
    await message.edit_text(cabinet_info.data, reply_markup=index_button.generate_to_info_button(), parse_mode='HTML')

async def go_to_balance_info(message: Message):
    await message.edit_text(balance_info.data, reply_markup=index_button.generate_to_info_button(), parse_mode='HTML')

async def go_to_trade_info(message: Message):
    await message.edit_text(trade_info.data, reply_markup=index_button.generate_to_info_button(), parse_mode='HTML')

async def go_to_main(message: Message):
    await message.edit_text(index_message.data, reply_markup=index_button.generate_index_button(), parse_mode='HTML')

async def go_to_info(message: Message):
    await message.edit_text(info_message.data,parse_mode='HTML', reply_markup=index_button.generate_info_button())

async def go_to_BTC_LTC(message: Message):
    await message.edit_text(index_message.data, reply_markup=index_button.generate_index_button(), parse_mode='HTML')

async def go_to_managment(message: Message):
    await message.edit_text(index_message.data, reply_markup=index_button.generate_index_button(), parse_mode='HTML')

async def go_to_balance_CB(message: Message):
    await message.edit_text(index_message.data, reply_markup=index_button.generate_index_button(), parse_mode='HTML')

async def go_to_balance(message: Message):
    await message.edit_text(index_message.data, reply_markup=index_button.generate_index_button(), parse_mode='HTML')

async def go_to_ADMIN_MENU(message: Message):
    await message.edit_text(index_message.data, reply_markup=index_button.generate_index_button(), parse_mode='HTML')