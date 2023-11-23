from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from acaiAplic.forms import ProdutoForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


class IndexView(TemplateView):
    template_name = 'index.html'

class EntrarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'entrar.html')

def register_page(request):
    return render(request, 'registro.html')



