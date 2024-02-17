# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User

# class Command(BaseCommand):
#     help = 'Create a user'

#     def handle(self, *args, **options):
#         #criar usuario
#         user = User.objects.create_user('lucastestecreat','email@dominio.com', 'senha123')
        
#         # Atribua permissões, se necessário
#         user.is_staff = True
#         user.is_superuser = True
#         user.save()

#         self.stdout.write(self.style.SUCCESS('Usuário criado com sucesso!'))

    