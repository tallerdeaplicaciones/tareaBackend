from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ticket, Tech
from .forms import TicketForm, CloseTicketForm, TechForm


class Home(ListView):
    model = Ticket
    #Opcional
    template_name = 'core/inicio.html'
    context_object_name = 'tickets'

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket/ticketForm.html'
    success_url = reverse_lazy('home')
    
class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket/ticketUpdate.html'
    success_url = reverse_lazy('home')

class TicketCloseView(UpdateView):
    model = Ticket
    form_class = CloseTicketForm
    template_name = 'ticket/ticketClose.html'
    success_url = reverse_lazy('home')


class TechCreateView(CreateView):
    model = Tech
    form_class = TechForm
    template_name = 'tech/techForm.html'
    success_url = reverse_lazy('home')

