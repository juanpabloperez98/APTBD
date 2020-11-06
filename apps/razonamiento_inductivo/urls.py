from django.urls import path
from . import views

app_name = 'razonamiento_inductivo_app'


urlpatterns = [
    path('razonamiento_inductivo',views.razonamiento_inductivo.as_view(),name = 'razonamiento_inductivo'),
    path('razonamiento_inductivo/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('razonamiento_inductivo/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('razonamiento_inductivo/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('razonamiento_inductivo/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('razonamiento_inductivo/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('razonamiento_inductivo/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]