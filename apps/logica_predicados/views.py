from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class logica_predicados(TemplateView):
    template_name = "teoria/logica_predicados/logica_predicados.html"