from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Meta(models.Model):
    titulo = models.CharField(max_length=200)
    criada_em = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo