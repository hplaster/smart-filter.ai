import requests
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("HG_API_KEY")

headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Lança exceção para erros HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


output = query({
	"inputs": {
	"source_sentence": "That is a happy person",
	"sentences": [
		"That is a happy dog",
		"That is a very happy person",
		"Today is a sunny day"
	]
},
})

print(output)
