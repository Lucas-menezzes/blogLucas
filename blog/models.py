from django.db import models
from django.utils import timezone

class GeneratedCPF(models.Model):
    name = models.CharField(max_length=255)
    date_birth = models.DateField()
    generated_cpf = models.CharField(max_length=11)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.generated_cpf}"
