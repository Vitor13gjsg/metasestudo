from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from core.models import Meta
from .forms import CadastroForm, LoginForm, MetaForm

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
    lista_metas = Meta.objects.all()
    context = {
        'lista_metas': lista_metas
    }
    return render(request, 'metas.html', context)

def area_cadastro(request):
    form = MetaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('metas')

    context = {
        'form': form
    }
    return render(request, 'area_cadastro.html', context)

def area_editar(request, id):
    meta = Meta.objects.get(pk=id)
    form = MetaForm(request.POST or None, instance=meta)

    if form.is_valid():
        form.save()
        return redirect('metas')

    context = {
        'form': form
    }
    return render(request, 'area_cadastro.html', context)

def area_remover(request, id):
    meta = Meta.objects.get(pk=id)
    meta.delete()
    return redirect('metas')

def sessoes(request):
    return render(request, "pages/sessoes.html")
   
@login_required(login_url="login")
def conta(request):
    return render(request, "pages/conta.html")

@login_required(login_url="login")
def alterar_senha(request):
    if request.method == "POST":
        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():
            usuario = form.save()
            update_session_auth_hash(request, usuario)

            messages.success(
                request,
                "Sua senha foi alterada com sucesso!"
            )

            return redirect("conta")
    else:
        form = PasswordChangeForm(request.user)

    return render(
        request,
        "pages/alterar_senha.html",
        {"form": form}
    )
   
@login_required(login_url="login")
def sair(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("conta")
