from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Produto, User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'preco', 'estoque', 'imagem']



