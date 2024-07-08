from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from unidecode import unidecode
from cpf_generator import CPF
from blog.models import GeneratedCPF
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
import json


class GerarCPFView(APIView): 
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    @csrf_exempt

    def post(self, request):
        try:
            content_type = request.META.get('CONTENT_TYPE', '')
            if 'application/json' in content_type:
                data = json.loads(request.body)
                name = data.get('name')
                date_birth_str = data.get('id_date_birth')
            else:
                name = request.POST.get('name')
                date_birth_str = request.POST.get('id_date_birth')

            date_birth = datetime.strptime(date_birth_str, '%Y-%m-%d').date()
            currentDate = datetime.now().date()

            #valida se data é maior que data atual
            if date_birth > currentDate:
                return JsonResponse({"error":'data não pode ser maior que data atual'}, status=400)
            #valida que o nome não pode ser vazio
            if not name:
                return JsonResponse({'error': 'nome não pode ser vazio'}, status=400)
            #valida que o nome não existe no banco
            if GeneratedCPF.objects.filter(name=name).exists():
                return JsonResponse({'error': 'nome ja esta cadastrado'}, status=400)
            
            cpf_gerado = CPF.generate()
                        
            generated_cpf = GeneratedCPF.objects.create(
                name=name,
                date_birth=date_birth,
                generated_cpf=str(cpf_gerado)
            )

            if 'application/json' in content_type:
                # Se a requisição aceita JSON, retorne JSON
                return JsonResponse({
                    'cpf': str(cpf_gerado),
                    'name': generated_cpf.name,
                    'date_birth': generated_cpf.date_birth,
                    'id': generated_cpf.id
                })
            else:
            #     # Caso contrário, renderize o HTML
                return render(request, 'blog/pages/index.html',{
                    'cpf': str(cpf_gerado),
                    'name': generated_cpf.name,
                    'date_birth': generated_cpf.date_birth,
                    'id': generated_cpf.id

                })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Erro ao decodificar JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class ListarCPFView(APIView): 

    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])

    def get(self, request):
        search_name = request.GET.get('name', None)
        search_id = request.GET.get('id', None)

        # Obter todos os objetos GeneratedCPF do banco de dados
        cpfs = GeneratedCPF.objects.all()
        if search_name:
            cpfs=cpfs.filter(name=search_name)
        if search_id:
            cpfs=cpfs.filter(id=search_id)

        content_type = request.META.get('CONTENT_TYPE', '')

        if 'application/json' in content_type:
            cpfs_data = [
                {
                    'id':cpf.id,
                    'name':cpf.name,
                    'date_birth':cpf.date_birth,
                    'cpf':cpf.generated_cpf,
                }
                for cpf in cpfs
            ]
            return JsonResponse({'cpfs': cpfs_data})
        else:
            return render(request, 'blog/pages/index.html', {'cpfs': cpfs})

    def search_cpf(request):
        ...