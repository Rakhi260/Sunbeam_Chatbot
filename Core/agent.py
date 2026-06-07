import os
import sys

os.environ["CHROMA_TELEMETRY"] = "False"
os.environ["ANONYMIZED_TELEMETRY"] = "False"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from langchain_openai import ChatOpenAI

from Core.agent_tools.greeting_tool import greeting_tool
from Core.agent_tools.sunbeam_rag_tool import sunbeam_rag_tool
from Core.agent_tools.fallback_tool import fallback_tool


llm = ChatOpenAI(
    model="gemini-2.5-flash",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ.get("GEMINI-API") or os.environ.get("GEMINI_API_KEY"),
    temperature=0.2
)


def router(user_input: str) -> str:
    """
    Routes user input to the correct tool.
    Greeting is matched safely (no substring bugs like 'hi' in 'with').
    """
    q = user_input.lower().strip()
    words = q.split()

    if len(words) <= 3 and any(
        w in {"hi", "hello", "hey", "thanks", "bye"} for w in words
    ):
        return greeting_tool.invoke(user_input)

    if any(
        w in {
            "sunbeam", "course", "courses",
            "branch", "branches",
            "internship", "internships",
            "fee", "fees",
            "schedule", "batch", "batches"
        }
        for w in words
    ):
        return sunbeam_rag_tool.invoke(user_input)

    return fallback_tool.invoke(user_input)


if __name__ == "__main__":
    print("🤖 Sunbeam Chatbot (router + tools, stable mode)\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            break

        response = router(user_input)
        print(f"\nBot: {response}\n")
