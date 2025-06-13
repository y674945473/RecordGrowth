#lc的记忆demo

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.llms import Ollama

llm = Ollama(
    base_url="http://localhost:11434",  # Ollama 默认端口
    model="deepseek-r1:7b",
    temperature=0.3,     # 控制创造性（0-1）
    num_ctx=4096         # 上下文长度
)

# 保留最近3轮对话历史
memory = ConversationBufferWindowMemory(k=3)
conversation = ConversationChain(llm=llm, memory=memory)

# 多轮对话示例
print(conversation.run("帮我写一个斐波那契数列的Python函数"))
print(conversation.run("添加类型注解"))
print(conversation.run("优化时间复杂度"))
