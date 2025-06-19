from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

import logging

# 设置全局日志级别为 DEBUG，显示所有详细信息
logging.basicConfig(level=logging.DEBUG)

embedding = OllamaEmbeddings(model="nomic-embed-text")
result = embedding.embed_query("LLM Powered Autonomous Agents\n    \nDate: June 23, 2023  |  Estimated Reading Time: 31 min  |")
  # 应输出一个高维向量长度，如 768 或 1024
print(result)
