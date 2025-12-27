import asyncio
import os
import threading
from flask import Flask

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from db import connect_db
from users import save_user
from handlers import handle_message
from keyboards import main_keyboard

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Fake web server for Render
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_web():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))

@dp.message(CommandStart())
async def start(message: Message):
    await save_user(message.from_user)
    await message.answer(
        "👋 Welcome!\nChoose an option:",
        reply_markup=main_keyboard()
    )

@dp.message()
async def all_messages(message: Message):
    reply = await handle_message(message)
    await message.answer(reply, reply_markup=main_keyboard())

async def main():
    await connect_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    asyncio.run(main())
