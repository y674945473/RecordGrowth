#1.安装智谱AI第三方库 pip install --upgrade zhipuai
#2.引入第三方库
from zhipuai import ZhipuAI
api_key = "xxx"
client = ZhipuAI(api_key=api_key)
prompt = '介绍一下你自己'
response = client.chat.completions.create(
    model='glm-4-flash',
    messages=[
        {"role":"user","content":"你好"},
        {"role":"assistant","content":"我是人工智能助手"},
        {"role":"user","content":prompt}
 
    ],
    #开通流式输出
    stream = True
)

# print(response.choices[0].message.content)
for chunk in response:
    print(chunk.choices[0].delta.content,end='')