"""
URL configuration for metasestudo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import (
    index, home, login, cadastro, materias, apagar_materia, metas, area_remover, sessoes,
    conta, alterar_senha, sair, pagina_informativa
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('termos/', pagina_informativa, {'pagina': 'termos'}, name='termos'),
    path('privacidade/', pagina_informativa, {'pagina': 'privacidade'}, name='privacidade'),
    path('contato/', pagina_informativa, {'pagina': 'contato'}, name='contato'),
    path('ajuda/', pagina_informativa, {'pagina': 'ajuda'}, name='ajuda'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('materias/', materias, name='materias'),
    path('materias/apagar/<int:materia_id>/', apagar_materia, name='apagar_materia'),
    path('metas/', metas, name='metas'),
    path('area_remover/<int:id>/', area_remover, name='area_remover'),
    path('sessoes/', sessoes, name='sessoes'),
    path('conta/', conta, name='conta'),
    path('alterar-senha/', alterar_senha, name='alterar_senha'),
    path('sair/', sair, name='sair'),
]

