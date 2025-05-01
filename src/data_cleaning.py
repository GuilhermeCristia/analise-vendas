import pandas as pd

def clean_data(df):
    # Remover valores faltantes
    df = df.dropna()
    
    # Converter tipos de dados
    df['data'] = pd.to_datetime(df['data'])
    df['valor'] = pd.to_numeric(df['valor'])
    
    # Salvar dados limpos
    df.to_csv('data/processed/vendas_limpo.csv', index=False)
    return df