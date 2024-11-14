from django.shortcuts import render, redirect 

# Create your views here.
from .forms import UsuarioForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


from django.contrib import messages
from .models import Usuario
from django.contrib.auth.hashers import check_password

def index(request):
    return render(request ,"pages/home.html")

def exercicio(request):
    return render (request, "pages/exercicio.html")

def cadastrar(request):
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        print(request.POST)  # Imprime os dados POST
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = make_password(form.cleaned_data['senha'])
            usuario.save()
            print("Redirecionando para a página de login", usuario)
            return redirect('/login/')  # Redireciona para a página de login após o registro
        else:
            print("Não funcionou")
    else:
        print("Cadastro não realizado")
        form = UsuarioForm()
        
    return render (request, "pages/cadastrar.html", {'form': form})


def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            # Busca o usuário pelo email
            usuario = Usuario.objects.get(email=email)
            
            # Verifica a senha
            if check_password(senha, usuario.senha):
                # Simula o login (você pode personalizar mais a autenticação aqui)
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nome'] = usuario.nome
                return redirect('perfil')  # Altere para a página de destino após o login
            else:
                messages.error(request, 'Senha incorreta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')
    
    return render(request, 'pages/login.html')

def logout(request):

    return redirect('login')  # Redireciona para a página de login após o logout


def perfil(request):
    
    return render(request, "pages/perfil.html")

def basico(request):
    
    return render(request, "pages/basico.html")