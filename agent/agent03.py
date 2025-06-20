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
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.output_parsers import StrOutputParser
 
#调用大语言模型
model = ChatZhipuAI(model_name='glm-4-flash')
 
# 创建返回的数据解析器
parser = StrOutputParser()
 
# 定义提示词模板
prompt_template = ChatPromptTemplate.from_messages([
    ('system','请将下面内容翻译成{language}'),
    ('human',"{text}")
])
 
#得到链
chain = prompt_template | model |parser
 
#调用chain
language = input('请输入你要选择的语言 /n')
text= input('请输入你要翻译的句子')
language = '"'+language+'"'
text = '"'+text+'"'
print(chain.invoke({'language':language,'text':text}))