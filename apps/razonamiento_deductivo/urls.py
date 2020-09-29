from django.urls import path
from . import views

app_name = 'razonamiento_deductivo_app'


urlpatterns = [
    path('razonamiento_deductivo',views.razonamiento_deductivo.as_view(),name = 'razonamiento_deductivo'),
]