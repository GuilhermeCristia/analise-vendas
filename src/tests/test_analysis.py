import pytest
import pandas as pd
from src.analysis import perform_analysis

@pytest.fixture
def sample_clean_data():
    return pd.DataFrame({
        'data': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
        'produto': ['Caneta', 'Caderno', 'Caneta'],
        'valor': [2.50, 15.90, 3.50],
        'quantidade': [10, 5, 8]
    })

def test_perform_analysis_basic_stats(sample_clean_data):
    results = perform_analysis(sample_clean_data)
    assert results['basic_stats']['total_vendas'] == pytest.approx(21.9)
    assert results['basic_stats']['quantidade_total'] == 23

def test_perform_analysis_temporal_stats(sample_clean_data):
    results = perform_analysis(sample_clean_data)
    assert len(results['temporal_stats']['vendas_por_mes']) == 1
    assert results['temporal_stats']['ticket_medio'] == pytest.approx(21.9/23)