import requests

def consultar_modelo_local(prompt):
    try:
        resposta = requests.post("http://localhost:11434/api/generate", json={
            "model": "mistral",
            "prompt": f"Gere código PyQGIS para: {prompt}\nResponda apenas com o código.",
            "stream": False
        })
        return resposta.json().get('response', '[Erro na resposta da IA]')
    except Exception as e:
        return f"[Erro ao conectar com o modelo local]: {e}"