from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from core.models import Meta, Materia
from .forms import CadastroForm, LoginForm, MetaForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "index.html")

def pagina_informativa(request, pagina):
    titulos = {
        "termos": "Termos",
        "privacidade": "Privacidade",
        "contato": "Contato",
        "ajuda": "Ajuda",
    }
    return render(request, "pages/info/informativa.html", {"titulo": titulos[pagina]})

def home(request):
    return render(request, "pages/app/home.html")

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

@login_required(login_url='login')
def materias(request):
    #  Matérias que aparecem na tela principal de matérias
    minhas_materias = Materia.objects.filter(
        Q(criador=request.user) | Q(usuarios=request.user)
    ).distinct()

    #  Matérias gerais do admin que aparecem na lista de adicionar matérias
    materias_gerais_disponiveis = Materia.objects.filter(is_visivel=True)

    if request.method == 'POST':
        materias_selecionadas_ids = request.POST.getlist('materias_existentes')
        nova_materia_nome = request.POST.get('nova_materia_texto', '').strip()
        is_admin = request.user.is_staff

        # Sincronizar as checkboxes das matérias gerais
        for materia in materias_gerais_disponiveis:
            if str(materia.id) in materias_selecionadas_ids:
                materia.usuarios.add(request.user)
            else:
                materia.usuarios.remove(request.user)

        # Criar nova matéria particular se preenchida
        if nova_materia_nome:
            nova_materia = Materia.objects.create(
                nome=nova_materia_nome,
                is_visivel=False, # É particular
                criador=request.user
            )
            nova_materia.usuarios.add(request.user)

        return redirect('materias')

    context = {
        'minhas_materias': minhas_materias,
        'materias_gerais_disponiveis': materias_gerais_disponiveis
    }

    return render(request, "pages/app/materias.html", context)

@login_required(login_url='login')
def apagar_materia(request, materia_id):
    # Só apaga se a matéria pertencer ao utilizador e for particular
    materia = get_object_or_404(Materia, id=materia_id, criador=request.user, is_visivel=False)
    
    if request.method == 'POST':
        materia.delete()
        
    return redirect('materias')

@login_required(login_url='login')
def metas(request):
    lista_metas = Meta.objects.filter(usuario=request.user).order_by('data_limite')
    hoje = timezone.localdate()

    # Editar uma meta específica
    meta_id = request.POST.get('meta_id') or request.GET.get('editar')
    meta_instancia = None
    if meta_id:
        meta_instancia = get_object_or_404(Meta, id=meta_id, usuario=request.user)

    if request.method == 'POST':
        form = MetaForm(request.POST, instance=meta_instancia, user=request.user)
        if form.is_valid():
            meta = form.save(commit=False)
            meta.usuario = request.user
            meta.save()
            return redirect('metas')
    else:
        form = MetaForm(user=request.user)

    context = {
        'lista_metas': lista_metas,
        'hoje': hoje,
        'form': form,
        'meta_editando': meta_instancia,
    }
    return render(request, "pages/app/metas.html", context)

def area_remover(request, id):
    meta = Meta.objects.get(pk=id)
    meta.delete()
    return redirect('metas')

def sessoes(request):
    return render(request, "pages/app/sessoes.html")
   
@login_required(login_url="login")
def conta(request):
    return render(request, "pages/account/conta.html")

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
        "pages/account/alterar_senha.html",
        {"form": form}
    )
   
@login_required(login_url="login")
def sair(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("conta")