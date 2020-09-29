from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class vectores(TemplateView):
    template_name = "teoria/vectores/vectores.html"