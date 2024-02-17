from dotenv import load_dotenv
load_dotenv()
import pytest
from django.urls import reverse
from faker import Faker
import json
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user_url():
    return reverse('create_user')

@pytest.fixture
def create_token_url():
    return reverse('user-login')

@pytest.fixture
def fake():
    return Faker()

def test_create_user(api_client, create_user_url, fake, db):
    username = fake.user_name()
    email = fake.email()
    password = 'senha123'

    user_data = {
        'username': username,
        'email': email,
        'password': password
    }

    json_data = json.dumps(user_data)
    response = api_client.post(create_user_url, data=json_data, content_type='application/json')
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['message'] =="User created successfully"
    assert User.objects.filter(username=username).exists()

def test_create_token(api_client, create_token_url, db):
    User.objects.create_user('lucasteste','tes@gmail.com','senha123')
    usernametk = 'lucasteste'
    passwordtk = 'senha123'

    data_token = {
        'username': usernametk,
        'password': passwordtk
    }

    json_data_tk = json.dumps(data_token)
    response = api_client.post(create_token_url, data=json_data_tk, content_type='application/json')
    response_data = response.json()
    assert response.status_code == 200
    assert 'access' in response_data

def test_user_invalid(api_client, create_token_url, db):
    data_invalid = {
        "username": "invalid",
        "password": "invalid"
    }

    json_data_invalid = json.dumps(data_invalid)
    response = api_client.post(create_token_url, data=json_data_invalid, content_type="application/json")
    assert response.status_code == 401
