import asyncio
import os
import threading
import psycopg2
from flask import Flask, request
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# ------------------------
# Flask app
# ------------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

@app.route("/admin")
def admin_panel():
    key = request.args.get("key")

    if key != ADMIN_KEY:
        return "❌ Access denied", 403

    cursor.execute("""
    SELECT telegram_id, text, created_at
    FROM messages
    ORDER BY created_at DESC
    LIMIT 100
    """)
    rows = cursor.fetchall()

    html = "<h1>Last Messages</h1><ul>"
    for r in rows:
        html += f"<li><b>{r[0]}</b>: {r[1]} ({r[2]})</li>"
    html += "</ul>"

    return html

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# ------------------------
# Environment variables
# ------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
ADMIN_KEY = os.getenv("ADMIN_KEY")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

if not ADMIN_KEY:
    raise RuntimeError("ADMIN_KEY is not set")

# ------------------------
# Database
# ------------------------
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE,
    username TEXT,
    first_name TEXT,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT,
    message_id BIGINT,
    text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    cursor.execute("""
    INSERT INTO users (telegram_id, username, first_name)
    VALUES (%s, %s, %s)
    ON CONFLICT (telegram_id) DO NOTHING
    """, (
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name
    ))
    conn.commit()

    await message.answer("✅ You are registered!")

@dp.message()
async def log_all_messages(message: Message):
    if not message.text:
        return

    cursor.execute("""
    INSERT INTO messages (telegram_id, message_id, text)
    VALUES (%s, %s, %s)
    """, (
        message.from_user.id,
        message.message_id,
        message.text
    ))
    conn.commit()

    await message.answer("📩 Message received")

async def run_bot():
    await dp.start_polling(bot)

# ------------------------
# Run
# ------------------------
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(run_bot())
