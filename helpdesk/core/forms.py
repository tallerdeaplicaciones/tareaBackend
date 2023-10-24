from django import forms
from .models import Ticket, Criticy, Tech

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'criticy', 'tech', 'status']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }