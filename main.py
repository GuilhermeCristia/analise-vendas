from src.data_cleaning import clean_data
from src.analysis import perform_analysis
from src.visualization import create_visualizations
import pandas as pd

def main():
    # Carregar dados
    raw_data = pd.read_csv('data/raw/vendas.csv')
    
    # Pipeline de análise
    clean_df = clean_data(raw_data)
    analysis_results = perform_analysis(clean_df)
    create_visualizations(clean_df)
    
    print("Análise concluída com sucesso!")

if __name__ == "__main__":
    main()