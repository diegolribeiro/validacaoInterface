from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def llm():
    return ChatOpenAI(
        model='gpt-3.5-turbo',
        temperature=0.0,
        api_key=os.getenv("OPENAI_API_KEY")
    )