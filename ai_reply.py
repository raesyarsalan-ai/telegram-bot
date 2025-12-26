def simple_ai_reply(user_text: str) -> str:
    user_text = user_text.lower()

    if "hello" in user_text or "hi" in user_text:
        return "Hello 👋 How can I help you today?"

    if "time" in user_text:
        return "⏰ I can help you manage your time better."

    if "motivation" in user_text:
        return "🔥 Keep going. Small steps every day create big results."

    return "🤖 I understand. Tell me more."
