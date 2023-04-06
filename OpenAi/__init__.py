import openai
import os
import httpx

openai.api_key = os.getenv("OPENAI_API_KEY")  # 设置 OpenAI API 密钥
proxy_url = "http://127.0.0.1:7980"  # 设置代理地址和端口号

# 设置代理客户端
proxies = {
    "http://": proxy_url,
    "https://": proxy_url,
}

http_client = httpx.Client(proxies=proxies)

# 发送带代理的请求
response = http_client.post(
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
