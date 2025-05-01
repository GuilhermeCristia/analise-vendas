import sys
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.analysis import perform_analysis
from src.data_cleaning import clean_data

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Configuração da página
st.set_page_config(page_title="Análise de Vendas", layout="wide")

# Título
st.title("📊 Dashboard de Análise de Vendas")

# Carregar dados
@st.cache_data
def load_data():
    raw_data = pd.read_csv('../data/raw/vendas.csv')
    clean_df = clean_data(raw_data)
    return perform_analysis(clean_df), clean_df

analysis_results, df = load_data()

# Sidebar com filtros
st.sidebar.header("Filtros")
selected_product = st.sidebar.multiselect(
    "Selecione os produtos:",
    options=df['produto'].unique(),
    default=df['produto'].unique()
)

# Aplicar filtros
filtered_df = df[df['produto'].isin(selected_product)]

# Métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("Total de Vendas", f"R${analysis_results['basic_stats']['total_vendas']:,.2f}")
col2.metric("Quantidade Vendida", f"{analysis_results['basic_stats']['quantidade_total']} unidades")
col3.metric("Ticket Médio", f"R${analysis_results['temporal_stats']['ticket_medio']:,.2f}")

# Gráficos
tab1, tab2, tab3 = st.tabs(["Vendas por Produto", "Vendas Mensais", "Distribuição"])

with tab1:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        x='produto', 
        y='valor', 
        data=filtered_df,
        estimator=sum,
        ci=None,
        ax=ax
    )
    ax.set_title("Vendas Totais por Produto")
    ax.set_ylabel("Valor Total (R$)")
    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(
        x='mes',
        y='valor',
        data=filtered_df,
        estimator=sum,
        ci=None,
        marker='o',
        ax=ax
    )
    ax.set_title("Vendas Mensais")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Valor Total (R$)")
    st.pyplot(fig)

with tab3:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(
        x='produto',
        y='valor',
        data=filtered_df,
        ax=ax
    )
    ax.set_title("Distribuição de Valores por Produto")
    st.pyplot(fig)

# Tabela de dados
st.header("Dados Detalhados")
st.dataframe(filtered_df)