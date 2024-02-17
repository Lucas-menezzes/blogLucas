from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login

@method_decorator(csrf_exempt, name="dispatch")
class CreateUserView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            
            # Autentique o usuário para gerar tokens
            authenticated_user = authenticate(request, username=data['username'], password=data['password'])
            login(request, authenticated_user)

            # Gere tokens de acesso e atualização
            refresh = RefreshToken.for_user(authenticated_user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return JsonResponse({'message': 'User created successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
class GetUserView(View):
    def get(self, request):
        try:
            users = User.objects.all()
            
            serialized_users = []

            for user in users:
                serialized_user = {'username': user.username}
                serialized_users.append(serialized_user)

            return JsonResponse({'users': serialized_users}, status=200)
        except Exception as e:
            return JsonResponse({'errors':str(e)}, status=500)