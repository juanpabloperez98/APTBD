from django.urls import path
from . import views

app_name = 'sistemas_ecuaciones_app'


urlpatterns = [
    path('sistemas_ecuaciones',views.sistemas_ecuaciones.as_view(),name = 'sistemas_ecuaciones'),
]