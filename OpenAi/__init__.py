import openai
import os
import requests

openai.api_key = os.getenv("OPENAI_API_KEY")  # 设置 OpenAI API 密钥


# 发送带代理的请求
response = requests.post(
    "https://api.openai.com/v1/engines/davinci-codex/completions",
    headers={"Authorization": f"Bearer {openai.api_key}"},
    json={
        "prompt": "关于人工智能的简介",
        "max_tokens": 30,
        "n": 1,
        "stop": "."
    }
)

# 输出生成的文本
print(response.json()["choices"][0]["text"])
