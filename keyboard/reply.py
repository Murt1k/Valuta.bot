from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 

keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "📋меню📋")],
        [KeyboardButton(text = "🆘помощь🆘")],
        [KeyboardButton(text = "📄о боте📄")]
    ],
    resize_keyboard = True
)



keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "💱калькулятор валют💱")],
        [KeyboardButton(text = "⚖️просмотр актуального курса⚖️")],
        [KeyboardButton(text = "‼️где купить или продать валюту‼️")]
    ],
    resize_keyboard = True
)
Kursik = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "EUR"),KeyboardButton(text = "JPY")],
        [KeyboardButton(text = "USD"),KeyboardButton(text = "AED")],
        [KeyboardButton(text = "CNY"),KeyboardButton(text = "BYN")],
        [KeyboardButton(text = "MORE")],
        [KeyboardButton(text = "коды валют")],
        [KeyboardButton(text = "🔙CANCEL🔙")]
    ],
    resize_keyboard = True
)

Calculator = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "EUR"),KeyboardButton(text = "JPY")],
        [KeyboardButton(text = "USD"),KeyboardButton(text = "AED")],
        [KeyboardButton(text = "CNY"),KeyboardButton(text = "BYN")],
        [KeyboardButton(text = "MORE")],
        [KeyboardButton(text = "коды валют")],
        [KeyboardButton(text = "🔙CANCEL🔙")]
    ],
    resize_keyboard = True
)
Nach_Calculator = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "1")],
        [KeyboardButton(text = "2")],
        [KeyboardButton(text = "🔙CANCEL🔙")]
    ],
    resize_keyboard = True
)