from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from ai import ask_ai

router = Router()

@router.message(Command("ai"))
async def ai_command(message: Message):
    await message.answer(
        "🧠 Send me your question and I will ask the AI.\n\nType your question now:"
    )

@router.message()
async def ai_message_handler(message: Message):
    user_text = message.text

    if not user_text:
        return

    await message.answer("⏳ Thinking...")

    ai_response = await ask_ai(user_text)

    await message.answer(ai_response)
