from django.shortcuts import render, redirect 

# Create your views here.
from .forms import UsuarioForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse



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
    
    return render (request, "pages/login.html")