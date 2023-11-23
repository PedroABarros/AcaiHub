from django.urls import path
from .views import IndexView
from .views import EntrarView
from acaiAplic import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('entrar/', EntrarView.as_view(), name='entrar'),
    path('registro/', views.register_page, name='registro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

