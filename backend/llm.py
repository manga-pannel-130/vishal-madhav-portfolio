# backend/llm.py

import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class LLMClient:
    """
    Handles communication with the Groq LLM.

    This class is responsible only for LLM communication.
    Archive knowledge and persona rules are handled by chatbot.py
    and persona.py.
    """

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GROQ_API_KEY is not configured. "
                "Create a .env file in the project root."
            )

        self.client = Groq(api_key=api_key)

        self.model = "openai/gpt-oss-120b"

    def generate_response(
        self,
        system_prompt: str,
        user_message: str,
        conversation_history: list | None = None,
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

        if conversation_history:
            messages.extend(conversation_history)

        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.2,
            max_completion_tokens=500,
        )

        content = response.choices[0].message.content

        if not content:
            return "I couldn't generate a response right now."

        return content.strip()