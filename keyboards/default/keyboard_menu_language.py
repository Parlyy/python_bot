from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ru π·πΊ'),
            KeyboardButton(text='Eng πΊπΈ')
        ]
    ],
    resize_keyboard=True
)


