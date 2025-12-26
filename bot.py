import asyncio
import os
import threading

from flask import Flask
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

# =====================
# Flask app (for Render)
# =====================
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# =====================
# Telegram Bot
# =====================
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# =====================
# Keyboard
# =====================
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Daily Suggestion")],
        [KeyboardButton(text="💬 Motivation")],
        [KeyboardButton(text="🛒 Smart Shopping List")],
    ],
    resize_keyboard=True
)

# =====================
# Handlers
# =====================
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🤖 Bot is alive!\nChoose an option:",
        reply_markup=main_keyboard
    )

@dp.message(F.text == "📅 Daily Suggestion")
async def daily_suggestion(message: Message):
    await message.answer(
        "📅 Today's suggestion:\nTake a 10-minute break and clear your mind 🌿"
    )

@dp.message(F.text == "💬 Motivation")
async def motivation(message: Message):
    await message.answer(
        "💬 Keep going.\nYou didn’t come this far to stop 💪"
    )

@dp.message(F.text == "🛒 Smart Shopping List")
async def shopping_list(message: Message):
    await message.answer(
        "🛒 Smart Shopping List:\n"
        "- Milk 🥛\n"
        "- Bread 🍞\n"
        "- Eggs 🥚"
    )

# =====================
# Run bot
# =====================
async def run_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(run_bot())
