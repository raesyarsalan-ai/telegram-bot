from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Bot Status")],
            [KeyboardButton(text="🛠 Tools")],
            [KeyboardButton(text="ℹ️ About Bot")]
        ],
        resize_keyboard=True
    )
    return keyboard
