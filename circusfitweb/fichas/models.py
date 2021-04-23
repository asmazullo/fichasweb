from django.db import models

# Create your models here.

from django.db import models


class Modalidade(models.Model):

    modalidade_nome = models.CharField(max_length=200)
    modalidade_pub_date = models.DateField(auto_now_add=True)


class Nivel(models.Model):

    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    nivel_ordem = models.IntegerField(default=1000)
    nivel_nome = models.CharField(max_length=200)
    nivel_pub_date = models.DateField(auto_now_add=True)


class Bloco(models.Model):

    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    bloco_ordem = models.IntegerField(default=1000)
    bloco_nome = models.CharField(max_length=200)
    bloco_pub_date = models.DateField(auto_now_add=True)


class Movimento(models.Model):

    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    movimento_dificuldade = models.CharField(max_length=1, default='A', choices=[('A','Muito Fácil: A'), ('B','Fácil: B'), ('C','Moderado: C'), ('D','Difícil: D'), ('E','Muito Difícil: E')])
    movimento_pub_date = models.DateField(auto_now_add=True)
    movimento_ativo = models.BooleanField(default=True)
    movimento_nome = models.CharField(max_length=200)
    movimento_explicacao = models.TextField(default='')
    movimento_ordem = models.IntegerField(default=10000)
