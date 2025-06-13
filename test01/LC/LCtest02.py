import openai
from ..myutil import httpUtil
from ..myutil import KeyUtil as keyUtil
# from openai import OpenAI

key = keyUtil.get_openai_key()
openai.api_key = key

httpUtil.get_completion("1+1是什么？")