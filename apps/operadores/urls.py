from django.urls import path
from . import views

app_name = 'operadores_app'


urlpatterns = [
    path('operadores',views.operadores.as_view(),name = 'operadores'),
    path('operadores/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('operadores/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('operadores/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('operadores/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('operadores/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('operadores/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]