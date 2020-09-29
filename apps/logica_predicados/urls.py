from django.urls import path
from . import views

app_name = 'logica_predicados_app'


urlpatterns = [
    path('logica_predicados',views.logica_predicados.as_view(),name = 'logica_predicados'),
]