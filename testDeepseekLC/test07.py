# 导入BeautifulSoup库中的SoupStrainer类，用于后续网页解析时只提取特定部分
import bs4

# 设置环境变量USER_AGENT，模拟浏览器请求头，用于网页抓取
import os
os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# 从langchain_community库中导入WebBaseLoader类，用于加载网页文档
from langchain_community.document_loaders import WebBaseLoader
#  从langchain_text_splitters库中导入RecursiveCharacterTextSplitter类，用于将文档进行分块
from langchain_text_splitters import RecursiveCharacterTextSplitter
# 从langchain_community库中导入Chroma类，用于将文档存储在Chroma数据库中
from langchain_community.vectorstores import Chroma
# # 从langchain_openai库中导入OpenAIEmbeddings类，用于将文档进行向量化
# from langchain_openai import OpenAIEmbeddings
# 从langchain_core库中导入LLMChain类，用于将LLM与输入进行交互
from langchain_core.output_parsers import StrOutputParser
# 从langchain_core库中导入LLM类，用于将输入转换为输出
from langchain_core.runnables import RunnablePassthrough
# 从langchain_hub库中导入hub模块，用于从hub中加载模型和工具
from langchain import hub
# 从langchain_community库中导入ollama类，用于使用ollama模型进行LLM
from langchain_community.llms import ollama

from langchain_ollama.embeddings import OllamaEmbeddings

import logging

from chromadb.config import Settings


# 启动命令 python -m testDeepseekLC.test07

# 设置全局日志级别为 DEBUG，显示所有详细信息
logging.basicConfig(level=logging.DEBUG)


# 返回本地模型的嵌入。在存储嵌入和查询时都需要用到此嵌入函数。
def  get_embedding():
    # nomic-embed-text: 一个高性能开放嵌入模型，具有较大的标记上下文窗口。
    # 安装：ollama pull nomic-embed-text:latest
    # 这个模型只有274M，但实际做嵌入和检索时，感觉比llama3这样的大模型还要好。
    embeddings = OllamaEmbeddings(model="nomic-embed-text",base_url="http://localhost:11434")  # Ollama默认端口
    return embeddings


# 创建SoupStrainer实例，仅解析网页中class为'post-title'、'post-header'和'post-content'的元素
bs4_strainer = bs4.SoupStrainer(class_=("post-title", "post-header", "post-content"))

# 实例化WebBaseLoader，指定要加载的网页路径和BeautifulSoup的解析配置
loader = WebBaseLoader(
    web_paths=('https://lilianweng.github.io/posts/2023-06-23-agent/',),
    bs_kwargs={"parse_only": bs4_strainer}
)

# 使用loader加载网页内容，并将结果存储在docs列表中
docs = loader.load()



# 输出加载的文档内容长度，以了解文档的大致规模
len(docs[0].page_content)

# 打印文档内容的前500个字符，用于预览和调试
print(docs[0].page_content[:500])

# 创建RecursiveCharacterTextSplitter实例，用于将文档进行分块
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
#  使用text_splitter将文档进行分块，并返回结果
all_splits = text_splitter.split_text(docs[0].page_content[:100])
print('=====================================================================')
print(all_splits)
print('=====================================================================')

# 指定Chroma数据库的持久化目录
persist_directory = 'chroma_langchain_db_test_2'

# 创建Chroma数据库实例，并传入文档和嵌入函数

try:
    client_settings = Settings(anonymized_telemetry=False)
    vectorstore = Chroma.from_texts(texts=all_splits, embedding=get_embedding(),persist_directory=persist_directory,client_settings=client_settings)
except Exception as e:
    print(f"发生异常：{e}")

print('1111111111111')

vectorstore.persist()

# 创建一个retriever实例，用于从Chroma数据库中检索文档
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
# 调用retriever的invoke方法，传入查询字符串，并返回检索到的文档
retrieved_docs = retriever.invoke("What are the approaches to Task Decomposition?")



# 创建一个prompt实例，用于生成提示
prompt = hub.pull("rlm/rag-prompt")
# 创建一个格式化文档的函数
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 配置本地模型
llm = ollama(
    base_url="http://localhost:11434",  # Ollama 默认端口
    model="deepseek-r1:7b",
    temperature=0.3,     # 控制创造性（0-1）
    num_ctx=4096         # 上下文长度
)

# 创建一个RAG链，将retriever、prompt和LLM连接起来
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 调用RAG链，传入查询字符串，并逐个打印输出
for chunk in rag_chain.stream("What is Task Decomposition?"):
    print(chunk, end="", flush=True)





