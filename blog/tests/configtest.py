from dotenv import load_dotenv
load_dotenv()
import pytest
from django.urls import reverse
from faker import Faker
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import json
import datetime
from blog.models import GeneratedCPF
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def fake():
    return Faker()

@pytest.fixture
def create_user_url():
    return reverse('create_user')

@pytest.fixture
def create_token_url():
    return reverse('user-login')

@pytest.fixture
def create_cpf_url():
    return reverse('gerar_cpf')

@pytest.fixture
def list_cpf_urls():
    return reverse('list_cpf')

@pytest.fixture
def create_token(db):
    user = User.objects.create_user('testuser', 'test@example.com', 'senha123')
    token= RefreshToken.for_user(user)
    return token.access_token

@pytest.fixture
def date_current():
    date_current= datetime.datetime.now().strftime('%Y-%m-%d')
    date_future= (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    return date_current, date_future

@pytest.fixture
def headers_auth(create_token):
    token=create_token
    headers = {'Authorization': f'Bearer {token}'}
    return headers

@pytest.fixture
def mock_generated_cpf():
    generated_cpf= GeneratedCPF.objects.create(
        name = "nome exist",
        date_birth = "2024-02-17",
        generated_cpf= "12345678901"
    )
    return generated_cpf

