from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class precedencia_operadores(TemplateView):
    template_name = "teoria/predencia_operadores/precedencia_operadores.html"