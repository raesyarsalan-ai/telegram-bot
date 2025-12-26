def simple_ai_reply(text: str) -> str:
    text = text.lower().strip()

    if text in ["hi", "hello", "hey"]:
        return "Hello 👋 How can I help you today?"

    if "who are you" in text:
        return "🤖 I am a smart assistant bot built to help you."

    if "motivation" in text:
        return "🔥 Stay consistent. Progress comes from daily action."

    if "help" in text:
        return "📌 You can use the buttons or just type your message."

    return "🤖 I understand. Please tell me more."
