from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db

#@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет', reply_markup=kb_client)
        await message.delete()
    except:
        await bot.send_message(message.from_user.id, 'Еще раз привет')

#@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Вт 9:00 - 20:00')

#@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная')

#@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
