def ask_ai(text: str) -> str:
    text = text.lower()

    if "hello" in text:
        return "Hello! How can I help you?"
    if "price" in text:
        return "Prices will be available soon."
    if "help" in text:
        return "Use the buttons below to navigate."

    return "I received your message 👍"
