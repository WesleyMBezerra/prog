from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

from .models import Questionario, Questao

class QuestionarioForm(forms.ModelForm):
    questoes = forms.ModelMultipleChoiceField(
        queryset=Questao.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Questionario
        fields = ['titulo', 'descricao', 'questoes', "prazo_disponibilidade"]
        widgets = {'prazo_disponibilidade':forms.DateTimeInput(attrs={'type':'datetime-local'}),}
