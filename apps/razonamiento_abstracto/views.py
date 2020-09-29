from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class razonamiento_abstracto(TemplateView):
    template_name = "teoria/razonamiento_abstracto/razonamiento_abstracto.html"