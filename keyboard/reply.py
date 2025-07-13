from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "Калькулятор валюты")],
        [KeyboardButton(text = "Простотр актуального курса")],
        [KeyboardButton(text = "Где купить или продать валюту")]
    ],
    resize_keyboard = True
)