import requests
import time
import pandas as pd

# Adicionar timer para não sobrecarregar a API
delay = 0.05

def get_response_to_dataframe(response):
    if response is not None:
        return pd.DataFrame(response['results'])
    else:
        return None

def get_complaints_by_vehicles(makes: list, models: list, model_year: int):
    """
    Obtém reclamações para múltiplas combinações de marcas e modelos em um determinado ano.
    
    Args:
        makes (list): Lista de marcas.
        models (list): Lista de modelos.
        model_year (int): Ano do modelo.
        delay (int/float): Tempo (em segundos) entre as requisições (padrão: 1).
    
    Returns:
        pd.DataFrame: DataFrame contendo as reclamações de todas as combinações de marca e modelo.
    """
    all_complaints = []  # Lista para armazenar todas as reclamações

    for make in makes:
        for model in models:
            url = f"https://api.nhtsa.gov/complaints/complaintsByVehicle?make={make}&model={model}&modelYear={model_year}"
            print(f"Buscando reclamações para Make: {make}, Model: {model}, Year: {model_year}...")

            response = requests.get(url)
            if response.status_code == 200:
                complaints = response.json().get('results', [])
                all_complaints.extend(complaints)  # Adiciona as reclamações à lista
            else:
                print(f"Erro ao acessar dados para Make: {make}, Model: {model}, Year: {model_year} ({response.status_code})")

            # Pausa para evitar sobrecarga na API
            time.sleep(delay)

    # Retorna um DataFrame com todas as reclamações encontradas
    return pd.DataFrame(all_complaints)
    

def get_model_years(issue_type='c'):
    url = f"https://api.nhtsa.gov/products/vehicle/modelYears?issueType={issue_type}"
    response = requests.get(url)
    
    if response.status_code == 200:
        time.sleep(delay)
        return get_response_to_dataframe(response.json())  # Retorna a lista de anos de modelo disponíveis
    else:
        print(f"Erro ao acessar dados: {response.status_code}")
        return None

def get_makes_by_model_year(model_year, issue_type='c'):
    url = f"https://api.nhtsa.gov/products/vehicle/makes?modelYear={model_year}&issueType={issue_type}"
    response = requests.get(url)
    
    if response.status_code == 200:
        time.sleep(delay)
        return get_response_to_dataframe(response.json())  # Retorna a lista de marcas para o ano do modelo
    else:
        print(f"Erro ao acessar dados: {response.status_code}")
        return None

def get_models_by_make_and_year(makes: list, model_year: int, issue_type='c'):
    all_models = []  # Lista para armazenar todos os modelos encontrados
    
    for make in makes:
        url = f"https://api.nhtsa.gov/products/vehicle/models?modelYear={model_year}&make={make}&issueType={issue_type}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = get_response_to_dataframe(response.json())  # Converte a resposta para DataFrame
            if data is not None and not data.empty:
                data['make'] = make  # Adiciona uma coluna para identificar a marca
                all_models.append(data)  # Adiciona os dados para essa marca
        else:
            print(f"Erro ao acessar dados para {make}: {response.status_code}")
    
    # Concatena todos os DataFrames em um único DataFrame
    if all_models:
        final_df = pd.concat(all_models, ignore_index=True)
        time.sleep(delay)
        return final_df
    else:
        print("Nenhum modelo encontrado.")
        return None


def get_complaints_by_vehicle_approach_b(make, model, model_year):
    url = f"https://api.nhtsa.gov/complaints/complaintsByVehicle?make={make}&model={model}&modelYear={model_year}"
    response = requests.get(url)
    
    if response.status_code == 200:
        time.sleep(delay)
        return get_response_to_dataframe(response.json())  # Retorna as reclamações para o modelo, marca e ano do modelo
    else:
        print(f"Erro ao acessar dados: {response.status_code}")
        return None

def get_complaints_by_odinumber(odinumber):
    url = f"https://api.nhtsa.gov/complaints/odinumber?odinumber={odinumber}"
    response = requests.get(url)
    
    if response.status_code == 200:
        time.sleep(delay)
        return get_response_to_dataframe(response.json())  # Retorna as reclamações para o número ODI fornecido
    else:
        print(f"Erro ao acessar dados: {response.status_code}")
        return None
