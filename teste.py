import pandas as pd

# Exemplo de leitura de diferentes formatos
def read_file(file_path):
    """
    Lê arquivos nos formatos XLSX, CSV e XML.
    """
    try:
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xml'):
            df = pd.read_xml(file_path, parser="etree")  # Necessário para XML (parser)
        else:
            raise ValueError("Formato não suportado. Use arquivos XLSX, CSV ou XML.")
    except Exception as e:
        raise ValueError(f"Erro ao processar o arquivo: {e}")
    return df


# Testando o carregamento de arquivos em um DataFrame
# df_xlsx = read_file("../MovimentaçãoMercantis_ORIGINAL.xlsx")
# print(df_xlsx.head())

# df_csv = read_file("archives/sample.csv")
# print(df_csv.head())

# df_xml = read_file("archives/artbreederGoblin.xml")
# print(df_xml.head())
