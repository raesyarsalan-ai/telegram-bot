import asyncio
import os
import threading
from flask import Flask

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from db import connect_db, save_message

# Fake web server for Render
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# Telegram bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("🤖 Bot is alive and connected to database!")

@dp.message()
async def message_handler(message: Message):
    await save_message(
        user_id=message.from_user.id,
        username=message.from_user.username,
        text=message.text
    )

    await message.answer("✅ Message saved.")

async def main():
    await connect_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(main())
