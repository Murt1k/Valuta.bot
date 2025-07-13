from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
start_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text="Ссылка",url="https://cbr.ru/") ],
        [InlineKeyboardButton(text="Документация",url="https://cbr.ru/currency_base/daily/")]
    ]
)
test_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = "test button", callback_data="test")]
    ]
)




