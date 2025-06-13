import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

def get_openai_key():
    _ = load_dotenv(Path('.')/'configMes.env')
    return os.environ['OPENAI_API_KEY']

# openai.api_key = get_openai_key()