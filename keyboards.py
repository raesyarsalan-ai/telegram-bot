from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💎 Upgrade")],
        [KeyboardButton(text="ℹ️ Help")]
    ],
    resize_keyboard=True
)
