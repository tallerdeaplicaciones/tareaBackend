from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ticket
from .forms import TicketForm
class Home(ListView):
    model = Ticket
    #Opcional
    template_name = 'core/inicio.html'
    context_object_name = 'ticket_list'

class Form(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket/ticketForm.html'
    success_url = reverse_lazy('ticket_form')
