from django.urls import path
from . import views

app_name = 'sistemas_ecuaciones_app'


urlpatterns = [
    path('sistemas_ecuaciones',views.sistemas_ecuaciones.as_view(),name = 'sistemas_ecuaciones'),
    path('sistemas_ecuaciones/ejemplo-1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('sistemas_ecuaciones/ejemplo-2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('sistemas_ecuaciones/ejemplo-3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('sistemas_ecuaciones/ejemplo-4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('sistemas_ecuaciones/ejemplo-5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('sistemas_ecuaciones/ejemplo-6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]