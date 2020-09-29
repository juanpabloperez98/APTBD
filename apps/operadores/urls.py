from django.urls import path
from . import views

app_name = 'operadores_app'


urlpatterns = [
    path('operadores',views.operadores.as_view(),name = 'operadores'),
]