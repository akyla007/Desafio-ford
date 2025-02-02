import pandas as pd
import ast
    
def process_products_dataframe(data: pd.DataFrame, output_filename: str) -> pd.DataFrame:
    """
    Processa a coluna de produtos em formato de string,
    explode a coluna para criar múltiplas linhas e normaliza os dados.
    
    :param data: Dados de entrada para criar o DataFrame
    :param output_filename: Nome do arquivo CSV de saída
    :return: DataFrame processado
    """
    df = pd.DataFrame(data)
    
    # Converter a string para listas de dicionários
    df['products'] = df['products'].apply(ast.literal_eval)
    
    # Explodir a coluna 'products'
    df_exploded = df.explode('products')
    
    # Transformar os dicionários da coluna 'products' em colunas separadas
    products_df = pd.json_normalize(df_exploded['products'])
    
    # Resetar os índices
    df_exploded.reset_index(drop=True, inplace=True)
    products_df.reset_index(drop=True, inplace=True)
    
    # Combinar os dados extraídos com o DataFrame original
    result = pd.concat([df_exploded.drop(columns=['products']), products_df], axis=1)
    
    # Salvar no arquivo CSV
    result.to_csv(f'../src/data/silver/{output_filename}.csv', index=False)
    
    return result

def drop_duplicated_and_null_rows(data: pd.DataFrame) -> pd.DataFrame:
    """
    Remove as linhas duplicadas e nulas de um DataFrame.
    
    :param data: Dados de entrada para remover as linhas duplicadas e nulas
    :return: DataFrame sem linhas duplicadas e nulas
    """
    df = pd.DataFrame(data)
    
    # Remover linhas duplicadas
    df.drop_duplicates(inplace=True)
    
    # Remover linhas nulas
    df.dropna(inplace=True)
    
    return df