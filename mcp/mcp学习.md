# mcp学习

## 环境准备
````
使用的包：langchain、LangGraph、langchain-mcp-adapters、DeepSeek
命令：（-U 升级当前包）
pip install -U langchain langgraph

pip install -U langchain-mcp-adapters

pip install -U langchain-deepseek
````

## 总结
````
就是将mcp服务当成一个工具提供者，将mcpserver中的工具提供给llm，让llm调用工具，完成任务
mcp服务中的工具是通过注解@mcp.tool 来声明出来，这样llm就能发现这些工具并进行调用
````