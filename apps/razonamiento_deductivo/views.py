from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class razonamiento_deductivo(TemplateView):
    template_name = "teoria/razonamiento_deductivo/razonamiento_deductivo.html"

class ejemplo1(TemplateView):
    template_name = "teoria/razonamiento_deductivo/ejemplos/ejemplo1.html"

class ejemplo2(TemplateView):
    template_name = "teoria/razonamiento_deductivo/ejemplos/ejemplo2.html"

class ejemplo3(TemplateView):
    template_name = "teoria/razonamiento_deductivo/ejemplos/ejemplo3.html"

class ejemplo4(TemplateView):
    template_name = "teoria/razonamiento_deductivo/ejemplos/ejemplo4.html"

class ejemplo5(TemplateView):
    template_name = "teoria/razonamiento_deductivo/ejemplos/ejemplo5.html"

class ejemplo6(TemplateView):
    template_name = "teoria/razonamiento_deductivo/ejemplos/ejemplo6.html"