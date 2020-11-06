from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class teoria_conjuntos(TemplateView):
    template_name = "teoria/teoria_conjuntos/teoria_conjuntos.html"

class ejemplo1(TemplateView):
    template_name = "teoria/teoria_conjuntos/ejemplos/ejemplo1.html"

class ejemplo2(TemplateView):
    template_name = "teoria/teoria_conjuntos/ejemplos/ejemplo2.html"

class ejemplo3(TemplateView):
    template_name = "teoria/teoria_conjuntos/ejemplos/ejemplo3.html"

class ejemplo4(TemplateView):
    template_name = "teoria/teoria_conjuntos/ejemplos/ejemplo4.html"

class ejemplo5(TemplateView):
    template_name = "teoria/teoria_conjuntos/ejemplos/ejemplo5.html"

class ejemplo6(TemplateView):
    template_name = "teoria/teoria_conjuntos/ejemplos/ejemplo6.html"