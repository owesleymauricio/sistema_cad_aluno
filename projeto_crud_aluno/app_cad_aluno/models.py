from django.db import models

class alunos(models.Model):
    id_alunos = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=250)
    nome_pai = models.TextField(max_length=250)
    nome_mae = models.TextField(max_length=250)
    data_nascimento = models.DateField()
    cep = models.IntegerField()
    rua = models.TextField(max_length=250)
    numero = models.IntegerField()
    complemento = models.TextField(max_length=250)