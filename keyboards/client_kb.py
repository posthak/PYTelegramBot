from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Working_hours')
b2 = KeyboardButton('/Address')
b3 = KeyboardButton('/Menu')
# b4 = KeyboardButton('Send mob number', request_contact=True)
# b5 = KeyboardButton('Send location', request_location=True)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).row(b2, b3,).row(b4, b5)
