from django.db import models
from django.contrib.auth.models import User

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    is_visivel = models.BooleanField(default=False)  # True = Geral (Admin), False = Particular
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materias_criadas')
    usuarios = models.ManyToManyField(User, related_name='materias_vinculadas', blank=True)

    def __str__(self):
        return self.nome


class Meta(models.Model):
    titulo = models.CharField(max_length=200)
    data_limite = models.DateField(null=True, blank=True)
    materia = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True, blank=True, related_name='metas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo