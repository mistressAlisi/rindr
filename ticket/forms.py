from django import forms
from django.forms import ModelForm,DateInput,Textarea,TextInput,Form
from .models import Ticket
from datetime import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['type','opened','responded','affirmer','notes','reference','contributors','fix']
        widgets = {
            'notes':'TextInput'
            },
    opened = forms.DateTimeField(widget=TextInput(attrs={"type": "datetime-local","step":1,"value":datetime.now().isoformat('T').split(".")[0]
}))
    responded = forms.DateTimeField(widget=TextInput(attrs={"type": "datetime-local","step":1,"value":datetime.now().isoformat('T').split(".")[0]
}))
    affirmer = forms.CharField(widget=TextInput(attrs={}))
    notes = forms.CharField(widget=TextInput(attrs={}))
    reference = forms.URLField(widget=TextInput(attrs={}))
    contributors = forms.CharField(widget=TextInput(attrs={}))


