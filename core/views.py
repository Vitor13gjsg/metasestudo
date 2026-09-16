from django.shortcuts import redirect, render
from metasestudo.form import CadastroForm
from metasestudo.form import LoginForm
from django.contrib.auth import login as auth_login

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
    return render(request, "pages/metas.html")

def configuracoes(request):
    return render(request, "pages/configuracoes.html")

def conta(request):
    return render(request, "pages/conta.html")