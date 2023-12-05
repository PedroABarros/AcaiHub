from django.urls import path
from .views import IndexView, lista_produtos, montar_pedido, finalizar_pedido
from .views import EntrarView
from acaiAplic import views
from django.conf.urls.static import static

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('entrar/', EntrarView.as_view(), name='entrar'),
    path('registro/', views.register_page, name='registro'),
    path('montar_pedido/', montar_pedido, name='montar_pedido'),
    path('lista_produtos/', lista_produtos, name='lista_produtos'),
    path('final_pedido/', finalizar_pedido, name='finalizar_pedido'),
]

