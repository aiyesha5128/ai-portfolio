
import asyncio
from semantic_kernel.contents import ChatHistory
from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings


import os
from dotenv import load_dotenv

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion


# Load environment variables from .env
load_dotenv()


def build_kernel() -> sk.Kernel:
    """
    Create and configure the Semantic Kernel instance.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    model_id = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")

    kernel = sk.Kernel()

    # Bind OpenAI chat completion service
    kernel.add_service(
        OpenAIChatCompletion(
            service_id="chat",
            api_key=api_key,
            ai_model_id=model_id
        )
    )

    return kernel


def run_prompt(prompt: str, context: str) -> str:
    """
    Create a prompt that includes retrieved context + the user question,
    then invoke Semantic Kernel chat completion.
    """
    kernel = build_kernel()

    full_prompt = f"""
Context:
{context}

Question:
{prompt}

Answer in a clear, helpful way:
"""

    async def _call_llm() -> str:
        chat = kernel.get_service("chat")

        history = ChatHistory()
        history.add_user_message(full_prompt)

        settings = OpenAIChatPromptExecutionSettings()
        response = await chat.get_chat_message_content(
            chat_history=history,
            settings=settings
        )

        # response usually has .content in newer SK versions
        return getattr(response, "content", str(response))

    return asyncio.run(_call_llm())


