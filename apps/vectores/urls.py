from django.urls import path
from . import views

app_name = 'vectores_app'


urlpatterns = [
    path('vectores', views.vectores.as_view(), name='vectores'),
    path('vectores/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('vectores/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('vectores/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('vectores/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('vectores/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('vectores/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]
