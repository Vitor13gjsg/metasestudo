from django.contrib import admin
from .models import Materia, Meta, Sessao

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'is_visivel', 'criador')
    list_filter = ('is_visivel',)
    search_fields = ('nome',)
