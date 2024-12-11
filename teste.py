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

'''
import pandas as pd
import requests
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity

# Carrega variáveis de ambiente
load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("HG_API_KEY")

headers = {"Authorization": f"Bearer {API_KEY}"}

# Função para consultar a API de embeddings
def get_embeddings(text_list):
    payload = {"inputs": text_list}
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()  # Verifica por erros HTTP
    return response.json()["embeddings"]

# Função principal para selecionar colunas
def process_table(file_path, columns_target):
    # Carregar a tabela
    df = pd.read_csv(file_path) if file_path.endswith(".csv") else pd.read_excel(file_path)

    # Gerar embeddings para os nomes das colunas
    col_names = df.columns.tolist()
    col_embeddings = get_embeddings(col_names)

    # Gerar embeddings para as colunas de referência
    ref_embeddings = get_embeddings(columns_target)

    # Calcular similaridade e selecionar colunas relevantes
    similarity_matrix = cosine_similarity(col_embeddings, ref_embeddings)
    selected_indices = [i for i in range(len(col_names)) if max(similarity_matrix[i]) > 0.8]  # Ajuste o limiar
    selected_columns = [col_names[i] for i in selected_indices]

    # Retornar DataFrame filtrado
    return df[selected_columns]

# Exemplo de uso
file_path = "exemplo_tabela.xlsx"
columns_target = ["data movimentacao", "valor pago", "quantidade"]
filtered_df = process_table(file_path, columns_target)

# Visualizar resultado
print(filtered_df.head())

'''