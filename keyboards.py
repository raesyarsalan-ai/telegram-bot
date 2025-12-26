from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🤖 About Bot")],
        [KeyboardButton(text="📞 Contact"), KeyboardButton(text="ℹ️ Help")]
    ],
    resize_keyboard=True
)
