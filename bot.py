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
    SELECT telegram_id, username, first_name, joined_at
    FROM users
    ORDER BY joined_at DESC
    """)
    users = cursor.fetchall()

    html = """
    <h1>Admin Panel</h1>
    <table border="1" cellpadding="5">
        <tr>
            <th>Telegram ID</th>
            <th>Username</th>
            <th>First Name</th>
            <th>Joined At</th>
        </tr>
    """

    for u in users:
        html += f"""
        <tr>
            <td>{u[0]}</td>
            <td>{u[1]}</td>
            <td>{u[2]}</td>
            <td>{u[3]}</td>
        </tr>
        """

    html += "</table>"
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

async def run_bot():
    await dp.start_polling(bot)

# ------------------------
# Run
# ------------------------
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(run_bot())
