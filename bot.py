import asyncio
import os
import threading
from flask import Flask

from aiogram import Bot, Dispatcher

from handlers import router


# Flask fake web server (for Render free web service)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )


# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)


async def run_bot():
    await dp.start_polling(bot)


if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(run_bot())
