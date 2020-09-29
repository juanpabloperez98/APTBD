from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class logica_predicados(TemplateView):
    template_name = "main/main.html"