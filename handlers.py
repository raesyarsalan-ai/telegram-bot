from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import main_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🤖 Bot is online and ready.",
        reply_markup=main_keyboard()
    )


@router.message(lambda message: message.text == "📊 Bot Status")
async def status_handler(message: Message):
    await message.answer(
        "✅ Status: Online\n⚡ Performance: Stable\n🌍 Server: Running"
    )


@router.message(lambda message: message.text == "🛠 Tools")
async def tools_handler(message: Message):
    await message.answer(
        "🛠 Available Tools:\n"
        "- Smart responses\n"
        "- Keyboard navigation\n"
        "- Cloud hosted bot"
    )


@router.message(lambda message: message.text == "ℹ️ About Bot")
from aiogram import F
from ai_reply import simple_ai_reply


@router.message(F.text)
async def ai_chat_handler(message: Message):
    reply = simple_ai_reply(message.text)
    await message.answer(reply)

async def about_handler(message: Message):
    await message.answer(
        "ℹ️ This is a Telegram bot built with Python and aiogram.\n"
        "Hosted on cloud and designed for scalability."
    )
