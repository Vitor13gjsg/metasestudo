from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "pages/home.html")

def login_view(request):
    return render(request, "auth/login.html")

def cadastro(request):
    return render(request, "auth/cadastro.html")

def materias(request):
    return render(request, "pages/materias.html")

def metas(request):
    return render(request, "pages/metas.html")

def configuracoes(request):
    return render(request, "pages/configuracoes.html")

def conta(request):
    return render(request, "pages/conta.html")