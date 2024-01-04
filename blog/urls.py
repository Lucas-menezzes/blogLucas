from django.urls import path
from blog.views import index, project, document, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('project/', project, name='project'),
    path('document/', document, name='document'),
    path('contact/', contact, name='contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)