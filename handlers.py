from aiogram.types import Message

async def handle_message(message: Message) -> str:
    text = message.text

    if text == "📅 Reminder":
        return "⏰ Don't forget to plan your day."

    if text == "💡 Suggestion":
        return "💡 Focus on one important task today."

    if text == "🔥 Motivation":
        return "🔥 Keep going. You're doing great."

    if text == "🤖 AI (soon)":
        return "🤖 AI is temporarily disabled."

    return "Please choose an option from the menu."
