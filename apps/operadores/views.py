from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class operadores(TemplateView):
    template_name = "teoria/operadores/operadores.html"

class ejemplo1(TemplateView):
    template_name = "teoria/operadores/ejemplos/ejemplo1.html"