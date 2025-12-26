from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import main_keyboard

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋 Welcome!\n\n"
        "This is a smart assistant bot.\n"
        "Choose an option below 👇",
        reply_markup=main_keyboard
    )

@router.message()
async def echo_handler(message: Message):
    if message.text == "🤖 About Bot":
        await message.answer("This bot is built with Python + aiogram 🚀")

    elif message.text == "📞 Contact":
        await message.answer("Contact: @your_username")

    elif message.text == "ℹ️ Help":
        await message.answer("Use the menu buttons to interact with the bot.")

    else:
        await message.answer(f"📝 You said:\n{message.text}")
