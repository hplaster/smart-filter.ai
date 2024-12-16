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
