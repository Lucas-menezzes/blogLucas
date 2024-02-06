from django.urls import path
from blog.views.create_user import CreateUserView
from blog.views.views import document, contact, films, index
from blog.views.create_document import gerar_cpf, list_cpf, index
from blog.views.climate_view import project
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from .views.login_view import UserLoginView
from rest_framework.permissions import IsAuthenticated

urlpatterns = [
    path('blog/', index, name='home'),
    path('project/', project, name='project'),
    path('document/', document, name='document'),
    path('contact/', contact, name='contact'),
    path('gerar_cpf/', gerar_cpf, name='gerar_cpf'),
    path('list_cpf/',authentication_classes([JWTAuthentication])(permission_classes([IsAuthenticated])(list_cpf)), name='list_cpf'),

    #urls de autenticação
    path('gerar_cpf/login/', UserLoginView.as_view(), name='user-login'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),

    ###CRUD Locadora ###
    path('films/', films, name='films'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)