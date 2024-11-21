from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('agent', 'Agent'),
        ('user', 'User'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    # Configurar email como el campo principal para autenticación
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Otros campos requeridos además del email
