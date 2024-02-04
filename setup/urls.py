
from django.contrib import admin
from django.urls import path, include
# from blog.views.views import index
from blog.views.climate_view import project


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
