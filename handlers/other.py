from aiogram import types
from aiogram import Dispatcher
import json, string
from create_bot import dp

# @dp.message_handler()
async def echo_send(message :types.Message):
    if {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cens.json')))) != set():
        await message.reply('Censorship is prohibited')
        await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)