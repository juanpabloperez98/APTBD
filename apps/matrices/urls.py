from django.urls import path
from . import views

app_name = 'matrices_app'


urlpatterns = [
    path('matrices',views.matrices.as_view(),name = 'matrices'),
]