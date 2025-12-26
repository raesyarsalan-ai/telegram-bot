import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

async def ask_ai(user_text: str) -> str:
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_text
        )

        return response.output_text

    except Exception as e:
        print("AI ERROR:", e)
        return "AI error. Please try again later."
