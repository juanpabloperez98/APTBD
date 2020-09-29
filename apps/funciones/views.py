from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class funciones(TemplateView):
    template_name = "teoria/funciones/funciones.html"