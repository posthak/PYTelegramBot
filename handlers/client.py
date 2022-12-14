from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards.client_kb import kb_client
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message :types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Bon Appetit!',reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Talking with Bot via private message, drop him a line :\n https://t.me/Deutschland_info_bot')

# @dp.message_handler(commands=['Working_hours'])
async def pizza_open_command(message :types.Message):
    await bot.send_message(message.from_user.id, 'Sun-Thu 9:00 20:00, Fri-Sat 10:00 23:00')


# @dp.message_handler(commands=['Address'])
async def pizza_address_command(message :types.Message):
    await bot.send_message(message.from_user.id, 'Hamburg, Munster Str 12',reply_markup=ReplyKeyboardRemove())

# # @dp.message_handler(commands=['Menu'])
# async def pizza_menu_command(message :types.Message):
#     for ret in cur.execute('SELECT * FROM menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0],f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Working_hours'])
    dp.register_message_handler(pizza_address_command, commands=['Address'])