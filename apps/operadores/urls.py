from django.urls import path
from . import views

app_name = 'operadores_app'


urlpatterns = [
    path('operadores',views.operadores.as_view(),name = 'operadores'),
    path('operadores/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
]