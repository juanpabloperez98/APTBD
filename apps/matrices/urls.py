from django.urls import path
from . import views

app_name = 'matrices_app'


urlpatterns = [
    path('matrices',views.matrices.as_view(),name = 'matrices'),
    path('matrices/ejemplo-1', views.ejemplo1.as_view(), name='ejemplo1'),
    path('matrices/ejemplo-2', views.ejemplo2.as_view(), name='ejemplo2'),
    path('matrices/ejemplo-3', views.ejemplo3.as_view(), name='ejemplo3'),
    path('matrices/ejemplo-4', views.ejemplo4.as_view(), name='ejemplo4'),
    path('matrices/ejemplo-5', views.ejemplo5.as_view(), name='ejemplo5'),
    path('matrices/ejemplo-6', views.ejemplo6.as_view(), name='ejemplo6'),
]