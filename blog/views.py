from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime

def index(request):
    city = 'salvador'
    uf = 'ba'
    country = 'br'
    start_date = '2024-01-21'
    end_date = '2024-01-22'

    url_api = f'http://localhost:8001/get_weather/{city}/{uf}/{country}/{start_date}/{end_date}'
    current_datetime= datetime.now()
    formatTime = current_datetime.strftime('%H:%M')

    try:
        requisition = requests.get(url_api)
        requisition.raise_for_status()
        data = requisition.json()
        
        temperatureCurrent = data.get("climate")[0].get("temperature") if data.get("climate") else "N/A"
        cityCurrent = data.get("city") or "unknown"
        descriptionCurrent = data.get("climate")[0].get("description") if data.get("climate") else "N/A"
        maxima=data.get("climate")[0].get("temp_max") if data.get("climate") else "N/A"
        minima=data.get("climate")[0].get("temp_min") if data.get("climate") else "N/A"
        
        return render(request, 'blog/pages/index.html', {
            'temperatureCurrent': temperatureCurrent, 
            'cityCurrent': cityCurrent,
            'descriptionCurrent': descriptionCurrent,
            'maxima': maxima,
            'minima': minima,
            'current_datetime': formatTime,
        })
                  
    except requests.exceptions.RequestException as erro:
        return render(request, 'blog/pages/index.html', {'error': str(erro)})
def project(request):
    return render(request, 'blog/pages/project.html')

def document(request):
    return render(request, 'blog/pages/documents.html')

def contact(request):
    return render(request, 'blog/pages/contact.html')

def films(request):
    return render(request, 'blog/films/films.html')