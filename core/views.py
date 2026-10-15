from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.db.models import Q

from core.models import Meta, Materia
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
    if request.method == 'POST':
        # Matérias selecionadas nas opções existentes
        materias_selecionadas_ids = request.POST.getlist('materias_existentes')

        # Texto digitado para criar uma nova matéria (se houver)
        nova_materia_nome = request.POST.get('nova_materia_texto', '').strip()

        # Identifica se o utilizador é administrador
        is_admin = request.user.is_staff

        # Vincula as matérias existentes selecionadas ao utilizador
        materias_para_vincular = Materia.objects.filter(id__in=materias_selecionadas_ids)
        for materia in materias_para_vincular:
            materia.usuarios.add(request.user)

        # Se o utilizador digitou uma nova matéria no campo de texto
        if nova_materia_nome:
            visibilidade = True if is_admin else False

            nova_materia = Materia.objects.create(
                nome=nova_materia_nome,
                is_visivel=visibilidade,
                criador=request.user
            )

            # Se for um utilizador normal, vincula automaticamente a ele
            if not is_admin:
                nova_materia.usuarios.add(request.user)
        return redirect('materias') # Redireciona de volta para a mesma página após salvar
    # Lógica para o GET: filtrar as matérias disponíveis para o usuário logado
    materias_disponiveis = Materia.objects.filter(
        Q(is_visivel=True) | Q(criador=request.user) | Q(usuario=request.user)
    ).distinct()

    context = {
        'materias_disponiveis': materias_disponiveis
    }

    return render(request, "pages/materias.html", context)

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