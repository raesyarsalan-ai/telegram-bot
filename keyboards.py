from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📅 Reminder")],
            [KeyboardButton(text="💡 Suggestion")],
            [KeyboardButton(text="🔥 Motivation")],
            [KeyboardButton(text="🤖 AI (soon)")]
        ],
        resize_keyboard=True
    )
