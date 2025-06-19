from langchain_community.llms import ollama

# 初始化 Ollama 连接
llm = ollama(
    base_url="http://localhost:11434",  # Ollama 默认端口
    model="deepseek-r1:7b",
    temperature=0.3,     # 控制创造性（0-1）
    num_ctx=4096         # 上下文长度
)
print(llm.invoke("Hello"))  # 应输出一段回复