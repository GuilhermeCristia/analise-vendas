import pytest
import pandas as pd
from src.data_cleaning import clean_data

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'data': ['2023-01-01', '2023-01-02', None],
        'produto': ['Caneta', None, 'Caderno'],
        'valor': ['2.50', '15.90', '3.50'],
        'quantidade': [10, 5, None]
    })

def test_clean_data_drops_nulls(sample_data):
    cleaned = clean_data(sample_data)
    assert cleaned.isnull().sum().sum() == 0

def test_clean_data_converts_types(sample_data):
    cleaned = clean_data(sample_data)
    assert pd.api.types.is_datetime64_any_dtype(cleaned['data'])
    assert pd.api.types.is_numeric_dtype(cleaned['valor'])