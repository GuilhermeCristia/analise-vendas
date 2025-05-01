import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='produto', y='valor', data=df)
    plt.title('Vendas por Produto')
    plt.savefig('outputs/figures/vendas_por_produto.png')
    plt.close()