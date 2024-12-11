import pandas as pd

# Exemplo de leitura de diferentes formatos
def read_file(file_path):
    if file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xml'):
        df = pd.read_xml(file_path, parser="etree") # pandas não possui conversor integrado de XML necessitando do argumento "parser".
    else:
        raise ValueError("Formato não suportado")
    return df

# Testando o carregamento de arquivos em um DataFrame
df_xlsx = read_file("../MovimentaçãoMercantis_ORIGINAL.xlsx")
print(df_xlsx.head())

df_csv = read_file("sample.csv")
print(df_csv.head())

df_xml = read_file("artbreederGoblin.xml")
print(df_xml.head())

