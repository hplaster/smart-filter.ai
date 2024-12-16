import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Carrega o modelo local
model = SentenceTransformer('all-MiniLM-L6-v2')

# Importando funções dos outros arquivos
from app import read_file

# Função para gerar embeddings
def get_embeddings(text_list):
    """
    Gera embeddings para uma lista de textos usando sentence-transformers localmente.
    """
    return model.encode(text_list, convert_to_numpy=True)


# Função principal para selecionar colunas
def process_table(file_path, columns_target):
    """
    Carrega o arquivo e filtra as colunas com base na similaridade semântica.
    """

    # Carrega a tabela usando a função read_file
    df = read_file(file_path)

    # Gerar embeddings para os nomes das colunas
    col_names = df.columns.tolist()
    col_embeddings = get_embeddings(col_names)
    # Gerar embeddings para as colunas de referência
    ref_embeddings = get_embeddings(columns_target)

    # Calcular similaridade e selecionar colunas relevantes
    similarity_matrix = cosine_similarity(col_embeddings, ref_embeddings)

    # Seleciona colunas relevantes com base no limiar
    selected_indices = [i for i in range(len(col_names)) if max(similarity_matrix[i]) > 0.8]  # Ajuste o limiar
    selected_columns = [col_names[i] for i in selected_indices]

    # Retornar DataFrame filtrado
    return df[selected_columns]

# Exemplo de uso
file_path = "../MovimentaçãoMercantis_ORIGINAL.xlsx"
columns_target = ["DATMOV", "CPF_CNPJ", "HISTORICO", "NRO_NFE", "razao social", "valor base", "banco", "valor-juros"]

filtered_df = process_table(file_path, columns_target)

# Visualizar resultado
print(filtered_df.head())
