from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import main_keyboard
from users import add_user, save_message, get_stats
from ai import ask_ai
from config import ADMIN_IDS

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    add_user(message.from_user)
    await message.answer(
        "🤖 Bot is alive!\nChoose an option:",
        reply_markup=main_keyboard
    )

@router.message()
async def message_handler(message: Message):
    save_message(message.from_user.id, message.text)

    if message.text == "📊 Statistics":
        if message.from_user.id in ADMIN_IDS:
            users, messages = get_stats()
            await message.answer(
                f"📊 Stats:\nUsers: {users}\nMessages: {messages}"
            )
        else:
            await message.answer("⛔ Admin only command.")
        return

    if message.text == "ℹ️ Help":
        await message.answer("This is a demo bot. More features soon.")
        return

    reply = ask_ai(message.text)
    await message.answer(reply)
