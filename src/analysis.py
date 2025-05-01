import pandas as pd
from datetime import datetime

def perform_analysis(df):
    # Análises básicas
    basic_stats = {
        'total_vendas': df['valor'].sum(),
        'media_vendas': df['valor'].mean(),
        'vendas_por_produto': df.groupby('produto')['valor'].sum().to_dict(),
        'quantidade_total': df['quantidade'].sum()
    }
    
    # Análises temporais
    df['data'] = pd.to_datetime(df['data'])
    df['mes'] = df['data'].dt.month
    df['dia_semana'] = df['data'].dt.day_name()
    
    temporal_stats = {
        'vendas_por_mes': df.groupby('mes')['valor'].sum().to_dict(),
        'vendas_por_dia': df.groupby('dia_semana')['valor'].sum().to_dict(),
        'ticket_medio': df['valor'].sum() / df['quantidade'].sum()
    }
    
    # Análise de desempenho
    df['valor_total'] = df['valor'] * df['quantidade']
    product_stats = df.groupby('produto').agg({
        'valor': 'mean',
        'quantidade': 'sum',
        'valor_total': 'sum'
    }).to_dict('index')
    
    return {
        'basic_stats': basic_stats,
        'temporal_stats': temporal_stats,
        'product_stats': product_stats,
        'raw_data': df.to_dict('records')
    }