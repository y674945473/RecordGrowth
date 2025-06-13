from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate

# 初始化 Ollama 连接
llm = Ollama(
    base_url="http://localhost:11434",  # Ollama 默认端口
    model="deepseek-r1:7b",
    temperature=0.3,     # 控制创造性（0-1）
    num_ctx=4096         # 上下文长度
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个Linux 性能调优专家，现在请回答客户的问题"),
    ("human", "{input}")
])

chain = prompt | llm
print(chain.invoke({"input": "CPU 使用率 100% 如何排查？"}))
