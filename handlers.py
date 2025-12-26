from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋 Welcome!\n\n"
        "This is a smart assistant bot.\n"
        "Use the menu below 👇"
    )

@router.message()
async def echo_handler(message: Message):
    await message.answer(
        f"📝 You said:\n{message.text}"
    )
