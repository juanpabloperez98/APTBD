from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class matrices(TemplateView):
    template_name = "teoria/matrices/matrices.html"


class ejemplo1(TemplateView):
    template_name = "teoria/matrices/ejemplos/ejemplo1.html"


class ejemplo2(TemplateView):
    template_name = "teoria/matrices/ejemplos/ejemplo2.html"


class ejemplo3(TemplateView):
    template_name = "teoria/matrices/ejemplos/ejemplo3.html"


class ejemplo4(TemplateView):
    template_name = "teoria/matrices/ejemplos/ejemplo4.html"


class ejemplo5(TemplateView):
    template_name = "teoria/matrices/ejemplos/ejemplo5.html"


class ejemplo6(TemplateView):
    template_name = "teoria/matrices/ejemplos/ejemplo6.html"