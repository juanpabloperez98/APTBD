from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class diagramas_flujo(TemplateView):
    template_name = "teoria/diagramas_flujo/diagramas_flujo.html"