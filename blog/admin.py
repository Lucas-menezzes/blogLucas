from django.contrib import admin

from django.contrib import admin
from .models import GeneratedCPF

class documents(admin.ModelAdmin):
    list_display = ('id', 'name', 'generated_cpf', 'date_birth')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 20

admin.site.register(GeneratedCPF, documents)

