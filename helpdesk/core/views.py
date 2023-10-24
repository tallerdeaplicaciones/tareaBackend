from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView


class Home():
    template_name = 'core/inicio.html'
    context_object_name = 'home'
