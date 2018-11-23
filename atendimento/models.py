from django.db import models

class Cliente(models.Model):    
    nome = models.CharField(max_length=50)
    dt_nasc = models.DateField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1)