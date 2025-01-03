# Dicionário de mapeamento das colunas necessárias
columns_mapping = {
    'data_movimentacao': ['DATA_MOV', 'DT_MOVI', 'DATA', 'DATE', 'data_movimentacao', 'data_movto', 'dt_mov'],
    'cnpj': ['CNPJ', 'CNPJ_EMPRESA', 'EMPRESA_ID'],
    'valor_total': ['VALOR_TOTAL', 'TOTAL_VAL', 'VALOR'],
    'valor_pago': ['valor_pago', 'vl_pago', 'pago'],
    'valor_recebido': ['valor_recebido', 'vl_recebido', 'recebido'],
    'valor_base': ['valor_base', 'vl_base', 'base'],
}

columns_description = {
    'data_movimentacao': 'Data em que a movimentação ocorreu',
    'valor_pago': 'Valor total pago em uma transação financeira',
    'valor_recebido': 'Valor total recebido de uma transação',
    'valor_base': 'Base de cálculo para a operação financeira',
}

# Exemplo pensando no Banco de Dados
columns_target = {
    "data_movimentacao": {
        "aliases": ["data movimentação", "dt_mov", "mov_date", "data"],
        "description": "Data em que a movimentação financeira ocorreu."
    },
    "valor_pago": {
        "aliases": ["valor pago", "vl_pago", "amount paid"],
        "description": "Montante pago em uma transação financeira."
    },
    "valor_recebido": {
        "aliases": ["valor recebido", "vl_recebido", "received value"],
        "description": "Montante recebido em uma transação financeira."
    }
}
