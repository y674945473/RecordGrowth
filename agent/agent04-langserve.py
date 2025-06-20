#安装第三方库  pip install langserve[all]
# 调用AI检测平台（langSmith）
import os
 
os.environ["LANGCHAIN_TRACING_V2"] = 'true'
os.environ['LANGSMITH_ENDPOINT'] = 'https://eu.api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = 'xxx'
os.environ['LANGCHAIN_PROJECT'] = '智谱AI测试'
 
#调用智谱AI API
os.environ["ZHIPUAI_API_KEY"] = "xxx"
 
#安装第三方库集成
#pip install langchain_community
#调用第三方库
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
# pip install langserve[all]
from langserve import add_routes
 
 
#调用大语言模型
model = ChatZhipuAI(model_name='glm-4-flash')
 
# 创建返回的数据解析器
parser = StrOutputParser()
 
# 定义提示模板
prompt_template = ChatPromptTemplate.from_messages([
      ('system','请将下面的内容翻译成{language}'),
      ('user',"{text}")
])
#得到链
chain = prompt_template | model | parser
 
 
#调用chain
print(chain.invoke({'language':'English','text':'今天心情非常好，因为中午吃了汉堡'}))
 
#创建fastAPI应用
app = FastAPI(title='我的Langchain服务',version='v1.0',description='使用Langchain翻译任何语句的服务器')

#添加路由
add_routes(
    app,
    chain,
    path="/chain"
 
)
 
if __name__ == "__main__":
    #构建服务器
    import uvicorn
 
    uvicorn.run(app,host="localhost",port=8000)