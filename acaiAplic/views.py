from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class EntrarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'entrar.html')