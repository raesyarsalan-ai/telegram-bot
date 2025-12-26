from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import main_keyboard
from ai_reply import simple_ai_reply
from users import save_user, increase_message_count, get_message_count

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    save_user(message.from_user.id, message.from_user.username)

    await message.answer(
        "🤖 Bot is alive!\n\nUse the buttons or type a message.",
        reply_markup=main_keyboard
    )


@router.message(F.text == "🔥 Daily Motivation")
async def motivation_handler(message: Message):
    await message.answer(
        "🔥 Today's motivation:\n"
        "Discipline beats motivation. Show up anyway."
    )


@router.message(F.text == "💳 Subscription")
async def subscription_handler(message: Message):
    await message.answer(
        "💳 Subscription Plans:\n\n"
        "Free: Limited messages\n"
        "Pro: Unlimited access (coming soon)"
    )


@router.message(F.text == "ℹ️ Help")
async def help_handler(message: Message):
    await message.answer(
        "ℹ️ You can:\n"
        "- Use buttons\n"
        "- Or type any message to chat with the bot"
    )


@router.message(F.text)
async def ai_chat_handler(message: Message):
    user_id = message.from_user.id

    save_user(user_id, message.from_user.username)
    increase_message_count(user_id)

    if get_message_count(user_id) > 20:
        await message.answer(
            "🚫 Free limit reached.\n"
            "Upgrade to Pro to continue."
        )
        return

    reply = simple_ai_reply(message.text)
    await message.answer(reply)
