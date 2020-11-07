from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class sistemas_ecuaciones(TemplateView):
    template_name = "teoria/sistemas_ecuaciones/sistemas_ecuaciones.html"

class ejemplo1(TemplateView):
    template_name = "teoria/sistemas_ecuaciones/ejemplos/ejemplo1.html"

class ejemplo2(TemplateView):
    template_name = "teoria/sistemas_ecuaciones/ejemplos/ejemplo2.html"

class ejemplo3(TemplateView):
    template_name = "teoria/sistemas_ecuaciones/ejemplos/ejemplo3.html"

class ejemplo4(TemplateView):
    template_name = "teoria/sistemas_ecuaciones/ejemplos/ejemplo4.html"

class ejemplo5(TemplateView):
    template_name = "teoria/sistemas_ecuaciones/ejemplos/ejemplo5.html"

class ejemplo6(TemplateView):
    template_name = "teoria/sistemas_ecuaciones/ejemplos/ejemplo6.html"