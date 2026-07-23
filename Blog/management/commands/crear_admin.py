import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Crea o actualiza la contraseña del superusuario a partir de variables de entorno'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')

        if not username or not password:
            self.stdout.write('DJANGO_SUPERUSER_USERNAME o DJANGO_SUPERUSER_PASSWORD no definidos: se omite.')
            return

        usuario, creado = User.objects.get_or_create(
            username=username, defaults={'email': email}
        )
        usuario.email = email or usuario.email
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(password)  # hashea la contraseña, nunca se guarda en texto plano
        usuario.save()

        if creado:
            self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" creado.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Contraseña de "{username}" actualizada.'))