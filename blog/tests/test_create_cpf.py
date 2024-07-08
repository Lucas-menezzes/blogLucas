import json
from configtest import create_token, mock_generated_cpf, api_client, fake, list_cpf_urls, create_cpf_url, create_token_url, headers_auth, date_current


#Testa criação de cpf
def test_create_cpf(api_client, create_cpf_url, headers_auth, date_current):
    current_date = date_current[0]
    headers = headers_auth
    cpf_data={
        "name": "teste22ernardi",
        "id_date_birth": current_date
    }

    data_format= json.dumps(cpf_data)
    response = api_client.post(create_cpf_url, data=data_format, content_type='application/json', headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data != None
    
#Testa se a data não é futura
def test_date_invalid(api_client, create_cpf_url, headers_auth, date_current):
    _, date_future= date_current
    headers = headers_auth
    cpf_data={
        "name": "teste22ernardi",
        "id_date_birth": date_future
    }

    data_format= json.dumps(cpf_data)
    response = api_client.post(create_cpf_url, data=data_format, content_type='application/json', headers=headers)
    response_data = response.json()
    assert response.status_code == 400
    assert response_data['error'] == "data não pode ser maior que data atual"

#Testa se o token está válido
def test_token_expired(api_client, create_cpf_url, date_current):
    current_date = date_current[0]
    token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4MTcyNzkwLCJpYXQiOjE3MDgxNzI0OTAsImp0aSI6IjRmMTRkMDI2ZDNhNjQ2ZThhYWRmMzUwOTgwYmJkZWQxIiwidXNlcl9pZCI6NH0.se7bzxo52o0OozNxyDQWPjUmyano9dkIl6EAdybNFHA'
    headers =  {'Authorization': f'Bearer {token}'}
    cpf_data={
        "name": "teste22ernardi",
        "id_date_birth": current_date
    }

    data_format= json.dumps(cpf_data)
    response = api_client.post(create_cpf_url, data=data_format, content_type='application/json', headers=headers)
    response_data = response.json()
    print(response_data)
    assert response.status_code == 401
    assert response_data['detail'] == "O token informado não é válido para qualquer tipo de token"
#Testa se nome ja existe
def test_create_name_exists(api_client, create_cpf_url, headers_auth, date_current, mock_generated_cpf):
    current_date = date_current[0]
    headers = headers_auth
    cpf_data={
        "name": mock_generated_cpf.name,
        "id_date_birth": current_date
    }
    data_format= json.dumps(cpf_data)
    response = api_client.post(create_cpf_url, data=data_format, content_type='application/json', headers=headers)
    response_data = response.json()
    assert response.status_code == 400
    assert response_data['error'] == "nome ja esta cadastrado"