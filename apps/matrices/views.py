from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class matrices(TemplateView):
    template_name = "teoria/matrices/matrices.html"