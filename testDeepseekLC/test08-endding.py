from langchain_ollama.embeddings import OllamaEmbeddings

embedding = OllamaEmbeddings(model="nomic-embed-text")
result = embedding.embed_query("This is a test sentence.")
print(len(result))  # 应输出一个高维向量长度，如 768 或 1024