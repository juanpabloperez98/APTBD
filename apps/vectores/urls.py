from django.urls import path
from . import views

app_name = 'vectores_app'


urlpatterns = [
    path('vectores',views.vectores.as_view(),name = 'vectores'),
]