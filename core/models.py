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
    concluida = models.BooleanField(default=False) # Permite marcar como concluída
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Sessao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessoes')
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE, related_name='sessoes')
    duracao_segundos = models.IntegerField(default=0) # Tempo cronometrado em segundos
    criada_em = models.DateTimeField(auto_now_add=True)

    def duracao_formatada(self):
        minutos = self.duracao_segundos // 60
        segundos = self.duracao_segundos % 60
        horas = minutos // 60
        minutos = minutos % 60
        if horas > 0:
            return f"{horas}h {minutos:02d}m {segundos:02d}s"
        return f"{minutos:02d}m {segundos:02d}s"

    def __str__(self):
        return f"Sessão - {self.meta.titulo} ({self.duracao_formatada()})"