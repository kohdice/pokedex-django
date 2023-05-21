from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "pokedex/index.html"


index = IndexView.as_view()
