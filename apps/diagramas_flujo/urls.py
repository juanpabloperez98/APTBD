from django.urls import path
from . import views

app_name = 'diagramas_flujo_app'


urlpatterns = [
    path('diagramas_flujo',views.diagramas_flujo.as_view(),name = 'diagramas_flujo'),
]