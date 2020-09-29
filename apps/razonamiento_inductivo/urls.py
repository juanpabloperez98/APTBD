from django.urls import path
from . import views

app_name = 'razonamiento_inductivo_app'


urlpatterns = [
    path('razonamiento_inductivo',views.razonamiento_inductivo.as_view(),name = 'razonamiento_inductivo'),
]