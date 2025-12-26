import asyncio
import os
import threading
from flask import Flask

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from db import create_tables

# -------------------
# Fake web server (for Render)
# -------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# -------------------
# Telegram Bot
# -------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("🤖 Bot is alive and database is ready!")

async def run_bot():
    await dp.start_polling(bot)

# -------------------
# Main
# -------------------
if __name__ == "__main__":
    # create tables once at startup
    create_tables()

    threading.Thread(target=run_flask).start()
    asyncio.run(run_bot())
