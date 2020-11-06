from django.urls import path
from . import views

app_name = 'razonamiento_abstracto_app'


urlpatterns = [
    path('razonamiento_abstracto',views.razonamiento_abstracto.as_view(),name = 'razonamiento_abstracto'),
    path('razonamiento_abstracto/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('razonamiento_abstracto/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('razonamiento_abstracto/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('razonamiento_abstracto/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('razonamiento_abstracto/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('razonamiento_abstracto/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]