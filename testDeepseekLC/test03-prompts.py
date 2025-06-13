from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

# 初始化模型
# llm = Ollama(model="deepseek-r1")

# 初始化 Ollama 连接
llm = Ollama(
    base_url="http://localhost:11434",  # Ollama 默认端口
    model="deepseek-r1:7b",
    temperature=0.3,     # 控制创造性（0-1）
    num_ctx=4096         # 上下文长度
)

# 创建提示模板
prompt = PromptTemplate(
    input_variables=["topic"],
    template="用中文写一首关于 {topic} 的五言绝句："
)

# 构建 Chain
chain = LLMChain(llm=llm, prompt=prompt)

# 执行调用
print(chain.run("秋天的枫叶"))
