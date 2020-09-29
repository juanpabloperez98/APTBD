from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class razonamiento_deductivo(TemplateView):
    template_name = "teoria/razonamiento_deductivo/razonamiento_deductivo.html"