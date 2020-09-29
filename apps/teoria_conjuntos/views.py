from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class teoria_conjuntos(TemplateView):
    template_name = "teoria/teoria_conjuntos/teoria_conjuntos.html"