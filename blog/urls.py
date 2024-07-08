from django.urls import path
from blog.views.create_user import CreateUserView, GetUserView
from blog.views.views import document, contact, films, index, login, calculator
from blog.views.create_document import GerarCPFView, ListarCPFView
from blog.views.climate_view import project
from django.conf import settings
from django.conf.urls.static import static
from .views.login_view import UserLoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('blog/', index, name='home'),
    path('project/', project, name='project'),
    path('document/', document, name='document'),
    path('contact/', contact, name='contact'),
    path('gerar_cpf/', GerarCPFView.as_view(), name='gerar_cpf'),
    path('list_cpf/', ListarCPFView.as_view(), name='list_cpf'),
    path('login/', login, name='login'), 
    path('calculator/', calculator, name='calculator'),
    

    #urls de autenticação
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('gerar_cpf/login/', UserLoginView.as_view(), name='user-login'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('get_user/', GetUserView.as_view(), name='get_user'),

    ###CRUD Locadora ###
    path('films/', films, name='films'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)