import os
from dotenv import load_dotenv
import argparse

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

langchain_tracing_v2 = os.getenv("LANGCHAIN_TRACING_V2")
langchain_endpoint = os.getenv("LANGCHAIN_ENDPOINT")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
langchain_project = os.getenv("LANGCHAIN_PROJECT")
openai_api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--stream",
        action="store_true",
        help="Enable streaming output",    
    )
    args = parser.parse_args()

    model = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=openai_api_key,
        temperature=0
    )

    messages = [
        SystemMessage("あなたは日本語を話すAIアシスタントです。"),
        HumanMessage("こんにちは、私の名前はカイトです。"),
        AIMessage(content="こんにちは、カイトさん！私はあなたのAIアシスタントです。何かお手伝いできることはありますか？"),
        HumanMessage(content="私の名前はわかりますか？"),
    ]

    if args.stream:
        for chunk in model.stream(messages):
            print(chunk.content, end="", flush=True)
    else:
        output = model.invoke(messages)
        print(output.content)
