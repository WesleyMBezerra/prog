"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name = "index"),
    path("exercicios/", views.exercicio, name="exercicios"),
    path("cadastrar/", views.cadastrar, name ="cadastrar"),
    path("login/", views.login, name ="login"),
    path('logout/', views.logout, name='logout'),
    path("perfil/", views.perfil, name="perfil"),
    path("basico/", views.basico, name="basico" ),
    path('questoes/', views.QuestaoListView.as_view(), name='lista_questoes'),
    path('questoes/nova/', views.QuestaoCreateView.as_view(), name='nova_questao'),
    path('questoes/<int:pk>/editar/', views.QuestaoUpdateView.as_view(), name='editar_questao'),
    path('questoes/<int:pk>/deletar/', views.QuestaoDeleteView.as_view(), name='deletar_questao'),
    path('questionarios/', views.QuestionarioListView.as_view(), name='lista_questionarios'),
    path('questionarios/novo/', views.QuestionarioCreateView.as_view(), name='novo_questionario'),
    path('questionarios/<int:pk>/', views.QuestionarioDetailView.as_view(), name='detalhe_questionario'),
    path('questionarios/<int:pk>/responder/', views.QuestionarioResponderView.as_view(), name='responder_questionario'),
    path('historico/', views.HistoricoRespostasView.as_view(), name='historico_respostas'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
