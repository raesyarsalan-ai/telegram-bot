from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔥 Daily Motivation")],
        [KeyboardButton(text="💳 Subscription")],
        [KeyboardButton(text="ℹ️ Help")]
    ],
    resize_keyboard=True
)
