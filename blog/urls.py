from django.urls import path
from blog.views.views import document, contact, films, index
from blog.views.create_document import gerar_cpf, list_cpf, index
from blog.views.climate_view import project
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog/', index, name='home'),
    path('project/', project, name='project'),
    path('document/', document, name='document'),
    path('contact/', contact, name='contact'),
    path('gerar_cpf/', gerar_cpf, name='gerar_cpf'),
    path('list_cpf/', list_cpf, name='list_cpf'),

    ###CRUD Locadora ###
    path('films/', films, name='films'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)