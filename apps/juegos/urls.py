from django.urls import path
from . import views

app_name = 'juegos_app'


urlpatterns = [
    path('juegos/juego1/index',views.juego1_index.as_view(),name = 'juego1-index'),
    path('juegos/juego1/indicaciones',views.juego1_indicaciones.as_view(),name = 'juego1-indicaciones'),
    path('juegos/juego1/play',views.juego1_play.as_view(),name = 'juego1-play'),


    path('juegos/juego2/index',views.juego2_index.as_view(),name = 'juego2-index'),
    path('juegos/juego2/indicaciones',views.juego2_indicaciones.as_view(),name = 'juego2-indicaciones'),
    path('juegos/juego2/play',views.juego2_play.as_view(),name = 'juego2-play'),



    path('juegos/juego3/index',views.juego3_index.as_view(),name = 'juego3-index'),
    path('juegos/juego3/indicaciones',views.juego3_indicaciones.as_view(),name = 'juego3-indicaciones'),
    path('juegos/juego3/play',views.juego3_play.as_view(),name = 'juego3-play'),


    path('juegos/juego4/index',views.juego4_index.as_view(),name = 'juego4-index'),
]