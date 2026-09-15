from django.shortcuts import redirect, render
from metasestudo.form import CadastroForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "pages/home.html")

def login(request):
    return render(request, "auth/login.html")

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home") 
        else:
            form = CadastroForm()
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