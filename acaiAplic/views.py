from typing import Any
from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from acaiAplic.forms import ProdutoForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from acaiAplic.models import Produto


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        return context

class EntrarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'entrar.html')

def register_page(request):
    return render(request, 'registro.html')

def montar_pedido(request):
    return render(request, 'base.html', {})

def finalizar_pedido(request):
    return render(request, 'finalPedido.html', {})

def lista_produtos(request):
    produtos = Produto.objects.all()

    query = request.GET.get('q')
    if query:
        produtos = produtos.filter(nome_produto__icontains=query)

    return render(request, 'sua_template.html', {'produtos': produtos})




