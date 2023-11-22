from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False


class Crud(models.Model):
    nome_responsavel = models.CharField(max_length=255, blank=False, null=False)
    nome_empresa = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)
    telefone = models.CharField(max_length=255, blank=False, null=False)
    cep = models.CharField(max_length=255, blank=False, null=False)
    endereco = models.CharField(max_length=255, blank=False, null=False)
    cidade = models.CharField(max_length=255, blank=False, null=False)
    estado = models.CharField(max_length=255, blank=False, null=False)
    seja = models.CharField(max_length=255, blank=False, null=False)
