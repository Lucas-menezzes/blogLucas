from django.shortcuts import render
import requests
from datetime import datetime
import locale

def project(request):
    if request.method == 'POST':
        city = request.POST.get('id_city')
        uf = request.POST.get('id_uf')
        country = request.POST.get('id_country')

        #pega todo json da api
        url_api = f'http://localhost:8000/get_weather/{city}/{uf}/{country}'
        current_datetime= datetime.now()
        formatTime = current_datetime.strftime('%H:%M')
        locale.setlocale(locale.LC_TIME, 'pt-br.UTF-8')
        
        #Valida a imagem que vai ser exbida a depender do horario do dia
        is_daytime = 6 <= current_datetime.hour < 18
        image_filename =  "ceu-estrelado.png" if not is_daytime else "ensolarado.jpg"
        image_path =  f"assets//imagens/{image_filename}"

        try:
            requisition = requests.get(url_api)
            requisition.raise_for_status()
            data = requisition.json()

            if 'climate' in data:
                temperature_data = data.get('climate')

                temperatureCurrent = data.get("climate")[0].get("temperature") if data.get("climate") else "N/A"
                cityCurrent = data.get("city") or "unknown"
                description_current = temperature_data[0].get("description") if temperature_data else "N/A"
                first_max_temp = float(temperature_data[0].get("temp_max"))
                first_min_temp = float(temperature_data[0].get("temp_min"))

                maxima_by_date = {}  # Dicionário para armazenar a maior temp_max por data
                minima_by_date = {}  # Dicionário para armazenar a menor temp_min por data

                for day_data in temperature_data:
                    date = day_data["date"].split(",")[0]
                    temp_max = float(day_data.get("temp_max"))
                    temp_min = float(day_data.get("temp_min"))

                    if date not in maxima_by_date or temp_max > maxima_by_date[date]:
                        maxima_by_date[date] = temp_max

                    if date not in minima_by_date or temp_min < minima_by_date[date]:
                        minima_by_date[date] = temp_min

                return render(request, 'blog/pages/project.html', {
                    'first_max': first_max_temp,
                    'first_min': first_min_temp,
                    'temperatureCurrent': temperatureCurrent, 
                    'cityCurrent': cityCurrent,
                    'descriptionCurrent': description_current,
                    'maxima': maxima_by_date,
                    'minima': minima_by_date,
                    'current_datetime': formatTime,
                    'image_path': image_path,

                })
            else:
                return render(request, 'blog/pages/project.html', {'error_message': 'Fudeu'})      
        except requests.exceptions.RequestException as erro:
            return render(request, 'blog/pages/project.html', {'error': str(erro)})
    return render(request, 'blog/pages/project.html', {})