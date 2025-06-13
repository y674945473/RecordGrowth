import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pathlib import Path


_ = load_dotenv(Path('.')/'configMes.env')

# 这里只是示意，工程中建议使用getpass.getpass()来获取API密钥
api_key = os.environ['DEEPSEEK_API_KEY']
api_base = "https://api.deepseek.com/"

# def simpleDemo():
#     """
#     简单的Langchain使用示例
#     """

#     model = init_chat_model(
#         model="deepseek-chat",
#         api_key=api_key,
#         api_base=api_base,
#         temperature=0.8,
#         max_tokens=1024,
#         model_provider="deepseek",
#     )

#     # messages = [
#     #     SystemMessage("Translate the following English text to Chinese"),
#     #     HumanMessage("Hello, how are you?")
#     # ]

#     # response = model.invoke(messages)
#     # print(response)

#     prompt = ChatPromptTemplate.from_messages([
#         SystemMessage("Translate the following English text to {language}"),
#         HumanMessage("{text}")
#     ])

#     messages = prompt.invoke({"language": "Chinese", "text":"Hello, how are you?"})
#     print(messages)
#     # for token in model.stream(messages):
#     #     print(token.content, end="", flush=True)
#     # print("\n\n")

# if __name__ == "__main__":
#     simpleDemo()
def promptTemplateDemo():
    """
    使用PromptTemplate的Langchain使用示例
    """
    model = init_chat_model(
        model="deepseek-chat",
        api_key=api_key,
        api_base=api_base,
        temperature=0.8,
        max_tokens=1024,
        model_provider="deepseek",
    )

    prompt = ChatPromptTemplate.from_messages([
        SystemMessage("Translate the following English text to {language}"),
        HumanMessage("{text}")
    ])

    messages = prompt.invoke({"language": "Chinese", "text":"Hello, how are you?"})
    response = model.invoke(messages)
    print(response)

if __name__ == "__main__":
    promptTemplateDemo()
