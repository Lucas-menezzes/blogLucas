from django.db import models

class GeneratedCPF(models.Model):
    name = models.CharField(max_length=255)
    date_birth = models.DateField()
    generated_cpf = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.name} - {self.generated_cpf}"
