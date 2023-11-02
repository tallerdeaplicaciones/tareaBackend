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
class TechForm(forms.ModelForm):
    class Meta:
        model = Tech
        fields = ['name', 'last_name', 'speciality']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'speciality': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class CloseTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['status']