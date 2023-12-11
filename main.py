import requests
import json
import os

chatgpt_key = os.getenv("OPENAI_API_KEY")
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

user_message = input("Insira sua mensagem: ")

body_mensagem = {
  "model": id_modelo,
  "messages": [{"role": "user", "content": user_message}]
}
body_mensagem = json.dumps(body_mensagem)

headers = {"Authorization": f"Bearer {chatgpt_key}", "Content-Type": "application/json"}
requisicao = requests.post(link, headers=headers, data=body_mensagem)

resposta = requisicao.json()
mensagem = "\n[ChatGPT]:\n" + resposta["choices"][0]["message"]["content"]

print(mensagem)