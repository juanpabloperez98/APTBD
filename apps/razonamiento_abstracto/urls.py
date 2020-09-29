from django.urls import path
from . import views

app_name = 'razonamiento_abstracto_app'


urlpatterns = [
    path('razonamiento_abstracto',views.razonamiento_abstracto.as_view(),name = 'razonamiento_abstracto'),
]