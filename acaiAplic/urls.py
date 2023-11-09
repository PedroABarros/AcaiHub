from django.urls import path
from .views import IndexView
from .views import EntrarView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('entrar/', EntrarView.as_view(), name='entrar'),
]

