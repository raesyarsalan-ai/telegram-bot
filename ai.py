import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

async def ask_ai(user_text: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful, friendly assistant."},
                {"role": "user", "content": user_text}
            ]
        )
        return response.choices[0].message.content
    except Exception:
        return "⚠️ AI error. Please try again later."
