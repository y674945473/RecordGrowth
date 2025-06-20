#LangSmish
#调用AI检测平台
#pip install langchain
import os
 
os.environ["LANGCHAIN_TRACING_V2"] = 'true'
os.environ['LANGSMITH_ENDPOINT'] = 'https://eu.api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = 'xxx'
os.environ['LANGCHAIN_PROJECT'] = '智谱AI测试'

#调用智谱AI API
os.environ["ZHIPUAI_API_KEY"] = 'xxx'
 
#安装第三方库集成
#pip install langchain_community
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
 
#调用语言大模型
model = ChatZhipuAI(model_name='glm-4-flash')
msg = [
    SystemMessage(content='请将以下内容翻译成英文'),
    HumanMessage(content='你好，我今天中午吃的汉堡')
]
# result = model.invoke(msg)
parser = StrOutputParser()
# print(parser.invoke(result))
 
#链式写法
chain = model | parser
#链式调用
print(chain.invoke(msg))