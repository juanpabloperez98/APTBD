from django.urls import path
from . import views

app_name = 'teoria_conjuntos_app'


urlpatterns = [
    path('teoria_conjuntos',views.teoria_conjuntos.as_view(),name = 'teoria_conjuntos'),
]