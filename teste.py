import requests
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

API_URL = os.getenv("API_URL")
headers = os.getenv("headers")

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
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
