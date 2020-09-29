from django.urls import path
from . import views

app_name = 'funciones_app'


urlpatterns = [
    path('funciones',views.funciones.as_view(),name = 'funciones'),
]