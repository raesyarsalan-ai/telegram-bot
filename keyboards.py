from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Daily Suggestion")],
        [KeyboardButton(text="💬 Motivation")],
        [KeyboardButton(text="🛒 Smart Shopping List")]
    ],
    resize_keyboard=True
)
