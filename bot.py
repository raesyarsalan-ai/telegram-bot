import asyncio
import os
import threading
from flask import Flask

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from db import connect_db, create_tables, add_user

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
    await add_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username
    )
    await message.answer("✅ You are saved in the database!")


async def main():
    await connect_db()
    await create_tables()
    await dp.start_polling(bot)


if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(main())
