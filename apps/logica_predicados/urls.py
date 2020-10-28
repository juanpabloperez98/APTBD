from django.urls import path
from . import views

app_name = 'logica_predicados_app'


urlpatterns = [
    path('logica_predicados',views.logica_predicados.as_view(),name = 'logica_predicados'),
    path('logica-predicados/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('logica-predicados/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('logica-predicados/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('logica-predicados/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('logica-predicados/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('logica-predicados/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6')
]