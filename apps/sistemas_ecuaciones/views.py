from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class sistemas_ecuaciones(TemplateView):
    template_name = "teoria/sistemas_ecuaciones/sistemas_ecuaciones.html"