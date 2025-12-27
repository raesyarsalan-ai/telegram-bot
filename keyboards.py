from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Statistics")],
        [KeyboardButton(text="ℹ️ Help")]
    ],
    resize_keyboard=True
)
