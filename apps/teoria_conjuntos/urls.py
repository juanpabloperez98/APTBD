from django.urls import path
from . import views

app_name = 'teoria_conjuntos_app'


urlpatterns = [
    path('teoria_conjuntos',views.teoria_conjuntos.as_view(),name = 'teoria_conjuntos'),
    path('teoria_conjuntos/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('teoria_conjuntos/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('teoria_conjuntos/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('teoria_conjuntos/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('teoria_conjuntos/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('teoria_conjuntos/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]