from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from ai import ask_ai

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🤖 Hello!\n"
        "Send me any message and I will reply using AI."
    )

@router.message()
async def ai_chat_handler(message: Message):
    user_text = message.text
    reply = await ask_ai(user_text)
    await message.answer(reply)
