from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import main_kb
from users import add_user, can_use, inc_usage, is_premium

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    add_user(message.from_user.id)
    await message.answer(
        "🤖 Welcome!\nFree users: 5 messages/day.",
        reply_markup=main_kb
    )

@router.message()
async def chat(message: Message):
    user_id = message.from_user.id

    if not is_premium(user_id):
        if not can_use(user_id):
            await message.answer("🚫 Daily limit reached. Upgrade to continue.")
            return
        inc_usage(user_id)

    await message.answer("✅ Message received.")
