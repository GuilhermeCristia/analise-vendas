def perform_analysis(df):
    analysis_results = {
        'total_vendas': df['valor'].sum(),
        'media_vendas': df['valor'].mean(),
        'vendas_por_produto': df.groupby('produto')['valor'].sum().to_dict()
    }
    return analysis_results