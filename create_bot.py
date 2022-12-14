from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = "5619440999:AAGVYf_v018LLUy21eUxcoPaNMuRuaf1JI0"
bot  = Bot(token = TOKEN)
dp = Dispatcher(bot,storage=storage)

