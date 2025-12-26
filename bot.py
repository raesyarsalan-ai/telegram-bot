import asyncio
import os
import threading
import psycopg2
from flask import Flask
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# ------------------------
# Flask app (keep Render alive)
# ------------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# ------------------------
# Environment variables
# ------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

# ------------------------
# Database connection
# ------------------------
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE,
    username TEXT,
    first_name TEXT,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()

# ------------------------
# Telegram bot
# ------------------------
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name

    cursor.execute("""
    INSERT INTO users (telegram_id, username, first_name)
    VALUES (%s, %s, %s)
    ON CONFLICT (telegram_id) DO NOTHING;
    """, (telegram_id, username, first_name))
    conn.commit()

    await message.answer("✅ You are registered!\nBot is connected to database.")

async def run_bot():
    await dp.start_polling(bot)

# ------------------------
# Run everything
# ------------------------
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(run_bot())
