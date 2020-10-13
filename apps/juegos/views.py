from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class juego1_index(TemplateView):
    template_name = "juegos/juego1/index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['game'] = 1
        return context


class juego1_indicaciones(TemplateView):
    template_name = "juegos/juego1/indicaciones.html"


class juego1_play(TemplateView):
    template_name = "juegos/juego1/play.html"


class juego2_index(TemplateView):
    template_name = "juegos/juego2/index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['game'] = 2
        return context


class juego2_indicaciones(TemplateView):
    template_name = "juegos/juego2/indicaciones.html"


class juego2_play(TemplateView):
    template_name = "juegos/juego2/play.html"


class juego3_index(TemplateView):
    template_name = "juegos/juego3/index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['game'] = 3
        return context


class juego3_indicaciones(TemplateView):
    template_name = "juegos/juego3/indicaciones.html"


class juego3_play(TemplateView):
    template_name = "juegos/juego3/play.html"


class juego4_index(TemplateView):
    template_name = "juegos/juego4/index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['game'] = 4
        return context

class juego4_indicaciones(TemplateView):
    template_name = "juegos/juego4/indicaciones.html"


class juego4_play(TemplateView):
    template_name = "juegos/juego4/play.html"
