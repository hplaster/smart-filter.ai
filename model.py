'''
    EXEMPLO COM AMOSTRAS DE REGISTROS JUNTO COM NOMES DAS COLUNAS
'''

from sentence_transformers import SentenceTransformer, util
import pandas as pd

# Modelo de similaridade semântica
modelo = SentenceTransformer('all-MiniLM-L6-v2')

# Descrições das colunas-alvo
descricoes_colunas = {
    'data_movimentacao': 'Data em que a movimentação ocorreu',
    'valor_pago': 'Valor que foi pago na transação',
    'valor_recebido': 'Valor que foi recebido na transação',
    'valor_base': 'Valor base utilizado no cálculo da transação',
}

# Carrega uma tabela de exemplo
arquivo = 'tabela_exemplo.xlsx'
df = pd.read_excel(arquivo)

# Função para prever categorias
def prever_colunas(df, descricoes_colunas, modelo):
    colunas_mapeadas = {}
    embeddings_descricoes = {k: modelo.encode(v) for k, v in descricoes_colunas.items()}

    for coluna in df.columns:
        # Cria embeddings para o nome e uma amostra dos valores
        nome_coluna = modelo.encode(coluna)
        conteudo_coluna = modelo.encode(" ".join(map(str, df[coluna].dropna().head(10))))

        # Calcula similaridade com descrições
        similaridades = {
            categoria: util.cos_sim(nome_coluna + conteudo_coluna, emb)[0].item()
            for categoria, emb in embeddings_descricoes.items()
        }

        # Associa à categoria com maior similaridade
        melhor_categoria = max(similaridades, key=similaridades.get)
        colunas_mapeadas[melhor_categoria] = df[coluna]

    return pd.DataFrame(colunas_mapeadas)

# Aplica a função
df_mapeado = prever_colunas(df, descricoes_colunas, modelo)
print(df_mapeado)
