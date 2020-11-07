from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class vectores(TemplateView):
    template_name = "teoria/vectores/vectores.html"


class ejemplo1(TemplateView):
    template_name = "teoria/vectores/ejemplos/ejemplo1.html"


class ejemplo2(TemplateView):
    template_name = "teoria/vectores/ejemplos/ejemplo2.html"


class ejemplo3(TemplateView):
    template_name = "teoria/vectores/ejemplos/ejemplo3.html"


class ejemplo4(TemplateView):
    template_name = "teoria/vectores/ejemplos/ejemplo4.html"


class ejemplo5(TemplateView):
    template_name = "teoria/vectores/ejemplos/ejemplo5.html"


class ejemplo6(TemplateView):
    template_name = "teoria/vectores/ejemplos/ejemplo6.html"
