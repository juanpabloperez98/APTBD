from django.urls import path
from . import views

app_name = 'precedencia_operadores_app'


urlpatterns = [
    path('precedencia_operadores',views.precedencia_operadores.as_view(),name = 'precedencia_operadores'),
]