from django.shortcuts import redirect, render
from metasestudo.form import CadastroForm, LoginForm, MetaForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required  # <--- ADICIONE ESTA LINHA AQUI
from core.models import Meta
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
# Create your views here.
def index(request):
   # if request.user.is_authenticated:
    #    return redirect("home")
    return render(request, "index.html")

def home(request):
    return render(request, "pages/home.html")

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
                auth_login(request, form.get_user())
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home") 
        return render(request, "auth/cadastro.html", {
            "form": form
        })
            
    return render(request, "auth/cadastro.html")

def materias(request):
    return render(request, "pages/materias.html")

def metas(request):
    if request.method == "POST":
        form = MetaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect("metas")
    else:
        form = MetaForm()

    lista_de_metas = Meta.objects.all().order_by('-criada_em')
    
    return render(request, "pages/metas.html", {"form": form, "metas": lista_de_metas})
    return render(request, "pages/metas.html", {"form": form, "metas": lista_de_metas})
def sessoes(request):
    return render(request, "pages/sessoes.html")
   
@login_required(login_url="login")
def conta(request):
    return render(request, "pages/conta.html")

