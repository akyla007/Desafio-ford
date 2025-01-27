import pandas as pd


def get_models_from_make_by_year(make: str, year: int):
    """
    Obtém os modelos de veículos de uma determinada marca e ano.
    
    Args:
        make (str): Marca do veículo.
        year (int): Ano do modelo.
    
    Returns:
        pd.DataFrame: DataFrame contendo os modelos de veículos da marca e ano especificados.
    """
    pd.read_csv('data/models.csv')