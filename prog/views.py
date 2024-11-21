from django.shortcuts import render, redirect, render, get_object_or_404 

# Create your views here.
from .forms import UsuarioForm
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse,  HttpResponseForbidden


from django.contrib import messages
from .models import Usuario, Questao, Questionario, RespostaUsuario
from django.contrib.auth import logout 


from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy

from .forms import QuestionarioForm


from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin




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

    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout


def perfil(request):
    
    
    return render(request, "pages/perfil.html")

def basico(request):
    
    return render(request, "pages/basico.html")

def verificar_resposta(request):
    if request.method == "POST":
        resposta = request.POST.get("answer")
        if resposta == "Hello World":
            return HttpResponse("Resposta correta!")
        else:
            return HttpResponse("Resposta incorreta. Tente novamente!")
    return redirect("basico")




class QuestaoListView(ListView):
    model = Questao
    template_name = 'pages/questoes/lista_questoes.html'
    context_object_name = 'questoes'
    


class QuestaoCreateView(CreateView):
    model = Questao
    fields = ['enunciado','imagem', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'resposta_correta']
    template_name = 'pages/questoes/form_questao.html'
    success_url = reverse_lazy('lista_questoes')



class QuestaoUpdateView(UpdateView):
    model = Questao
    fields = ['enunciado','imagem', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'resposta_correta']
    template_name = 'pages/questoes/form_questao.html'
    success_url = reverse_lazy('lista_questoes')

class QuestaoDeleteView(DeleteView):
    model = Questao
    template_name = 'pages/questoes/confirm_delete.html'
    success_url = reverse_lazy('lista_questoes')


class QuestionarioCreateView(CreateView):
    model = Questionario
    form_class = QuestionarioForm
    template_name = 'pages/questoes/form_questionario.html'
    success_url = reverse_lazy('lista_questionarios')

class QuestionarioListView(ListView):
    model = Questionario
    template_name = 'pages/questoes/lista_questionario.html'
    context_object_name = 'questionarios'

class QuestionarioDetailView(DetailView):
    model = Questionario
    template_name = 'pages/questoes/detalhe_questionario.html'
    context_object_name = 'questionario'
    


class QuestionarioResponderView(TemplateView):
    template_name = 'pages/questoes/responder_questionario.html'

    def post(self, request, *args, **kwargs):
        questionario = get_object_or_404(Questionario, pk=self.kwargs['pk'])
        

        respostas = {}
        pontuacao = 0

        for questao in questionario.questoes.all():
            resposta_usuario = request.POST.get(f'questao_{questao.id}')
            if not resposta_usuario:
                return render(request, 'pages/questoes/responder_questionario.html', {
                                'questionario': questionario,
                                'error_message': "Por favor, selecione uma resposta para todas as questões."
             })

            correta = resposta_usuario == questao.resposta_correta
            if correta:
                pontuacao += 1

            RespostaUsuario.objects.create(
                usuario=request.user if request.user.is_authenticated else None,
                questionario=questionario,
                questao=questao,
                resposta=resposta_usuario,
                correta=correta
            )

            respostas[questao.id] = {
                'resposta_usuario': resposta_usuario,
                'correta': correta
            }

        return render(request, 'pages/questoes/resultado_questionario.html', {
            'questionario': questionario,
            'respostas': respostas,
            'pontuacao': pontuacao,
            'total_questoes': questionario.questoes.count()
        })

        


class HistoricoRespostasView(ListView):
    model = RespostaUsuario
    template_name = 'pages/questoes/historico_respostas.html'
    context_object_name = 'respostas'

    def get_queryset(self):
        return RespostaUsuario.objects.filter(usuario=self.request.user).order_by('-id')



