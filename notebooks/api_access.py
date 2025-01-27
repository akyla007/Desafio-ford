import requests
import pandas as pd

def get_response_to_dataframe(response):
    if response is not None:
        return pd.DataFrame(response['results'])
    else:
        return None

def get_complaints_by_vehicle(make, model, model_year):
    url = f"https://api.nhtsa.gov/complaints/complaintsByVehicle?make={make}&model={model}&modelYear={model_year}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return get_response_to_dataframe(response.json())  # Retorna a resposta JSON com as reclamações
    else:
        print(f"Erro ao acessar dados: {response.status_code}")
        return None

def get_model_years(issue_type='c'):
    url = f"https://api.nhtsa.gov/products/vehicle/modelYears?issueType={issue_type}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return get_response_to_dataframe(response.json())  # Retorna a lista de anos de modelo disponíveis
    else:
        print(f"Erro ao acessar dados: {response.status_code}")
        return None

def get_makes_by_model_year(model_year, issue_type='c'):
    url = f"https://api.nhtsa.gov/products/vehicle/makes?modelYear={model_year}&issueType={issue_type}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return get_response_to_dataframe(response.json())  # Retorna a lista de marcas para o ano do modelo
    else:
        print(f"Erro ao acessar dados: {response.status_code}")
        return None

def get_models_by_make_and_year(make, model_year, issue_type='c'):
    url = f"https://api.nhtsa.gov/products/vehicle/models?modelYear={model_year}&make={make}&issueType={issue_type}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return get_response_to_dataframe(response.json())  # Retorna a lista de modelos para a marca e ano do modelo
    else:
        print(f"Erro ao acessar dados: {response.status_code}")
        return None

def get_complaints_by_vehicle_approach_b(make, model, model_year):
    url = f"https://api.nhtsa.gov/complaints/complaintsByVehicle?make={make}&model={model}&modelYear={model_year}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return get_response_to_dataframe(response.json())  # Retorna as reclamações para o modelo, marca e ano do modelo
    else:
        print(f"Erro ao acessar dados: {response.status_code}")
        return None

def get_complaints_by_odinumber(odinumber):
    url = f"https://api.nhtsa.gov/complaints/odinumber?odinumber={odinumber}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return get_response_to_dataframe(response.json())  # Retorna as reclamações para o número ODI fornecido
    else:
        print(f"Erro ao acessar dados: {response.status_code}")
        return None
