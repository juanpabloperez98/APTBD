from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class razonamiento_inductivo(TemplateView):
    template_name = "teoria/razonamiento_inductivo/razonamiento_inductivo.html"