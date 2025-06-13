from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain.agents import AgentType, initialize_agent, Tool
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# 自定义文学分析工具（无需API）
class BookQuotesTool:
    @staticmethod
    def search_quotes(book_title: str, author: str = "木心") -> str:
        """模拟文学语录检索（实际可接入本地知识库）"""
        quotes_db = {
            "素履之往": [
                "生命好在无意义，才容得下各自赋予意义。",
                "所谓无底深渊，下去，也是前程万里。",
                "岁月不饶人，我亦未曾饶过岁月。"
            ]
        }
        return "\n".join(quotes_db.get(book_title, ["暂未收录该作品语录"]))

# 配置本地模型
llm = Ollama(
    base_url="http://localhost:11434",  # Ollama 默认端口
    model="deepseek-r1:7b",
    temperature=0.3,     # 控制创造性（0-1）
    num_ctx=4096         # 上下文长度
)
chat_model = ChatOllama(model="deepseek-r1:7b")

# 初始化记忆系统
memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    k=5,
    return_messages=True
)

# 构建定制化工具集
tools = [
    Tool(
        name="LiteratureSearch",
        func=lambda query: BookQuotesTool.search_quotes("素履之往"),
        description="用于检索木心《素履之往》的经典语录"
    ),
    WikipediaQueryRun(
        api_wrapper=WikipediaAPIWrapper(top_k_results=1, lang="zh")
    )
]

# 创建带文学分析能力的Agent
agent = initialize_agent(
    tools,
    chat_model,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=3  # 限制搜索深度
)

# 测试用例
queries = [
    "列举《素履之往》中关于时间的哲理语句",
    "这本书里如何阐述生命的意义？",
    "将第二句语录用英文翻译"
]

for q in queries:
    print(f"问题：{q}")
    print(agent.run(q))
    print("\n" + "="*50 + "\n")
