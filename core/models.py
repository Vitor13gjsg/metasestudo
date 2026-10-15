from django.db import models
from django.contrib.auth.models import User

class Meta(models.Model):
    titulo = models.CharField(max_length=200)
    criada_em = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=7, default="#FFFFFF") # Código HEX da cor
    is_visivel = models.BooleanField(default=True) # True para Admin

    # Quem criou a matéria (admin ou usuário normal)
    criador = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='materias_criadas',
    )

    # Relação "Vincular" (muitos para muitos) entre Usuário e Matéria
    usuarios = models.ManyToManyField(
        User,
        related_name='materias_vinculadas',
        blank=True,
    )

    def __str__(self):
        return self.nome