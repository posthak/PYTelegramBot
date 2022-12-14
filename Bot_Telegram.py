from aiogram.utils import executor
from create_bot import dp

async def on_startup(_):
    print('Bot is online now')

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


    # await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp,skip_updates=True, on_startup=on_startup)