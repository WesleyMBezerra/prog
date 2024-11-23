from django.db import models

from django.contrib.auth.models import AbstractUser, User

from django.conf import settings

from django.utils.timezone import now
from datetime import timedelta

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Questao(models.Model):
    enunciado = models.TextField()
    imagem = models.ImageField(upload_to='questoes/', blank=True, null=True)
    alternativa_a = models.CharField(max_length=255)
    alternativa_b = models.CharField(max_length=255)
    alternativa_c = models.CharField(max_length=255)
    alternativa_d = models.CharField(max_length=255)
    resposta_correta = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return self.enunciado
    
    
class Questionario(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    questoes = models.ManyToManyField('Questao', related_name='questionarios')

    def __str__(self):
        return self.titulo
    
 
class RespostaUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    questionario = models.ForeignKey('Questionario', on_delete=models.CASCADE)
    questao = models.ForeignKey('Questao', on_delete=models.CASCADE)
    resposta = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    correta = models.BooleanField()

    def __str__(self):
        return f"Resposta: {self.questao.enunciado} - {'Correta' if self.correta else 'Incorreta'}"

    
    