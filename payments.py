from aiogram.types import Message
from aiogram import Router
from config import USDT_WALLET, ADMIN_IDS
from users import activate_premium

router = Router()

@router.message(lambda m: m.text == "💎 Upgrade")
async def upgrade(message: Message):
    await message.answer(
        f"💳 Premium (1 Year)\n\n"
        f"Send **20 USDT (TRC20)** to:\n\n"
        f"`{USDT_WALLET}`\n\n"
        f"Then send TXID here."
    )

@router.message(lambda m: len(m.text) > 30)
async def txid_handler(message: Message):
    for admin in ADMIN_IDS:
        await message.bot.send_message(
            admin,
            f"💰 Payment Request\nUser: {message.from_user.id}\nTXID:\n{message.text}"
        )
    await message.answer("⏳ Payment sent for review.")
