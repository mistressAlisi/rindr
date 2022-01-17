from django.forms import ModelForm,CharField,TextInput
from .models import Cause

class CauseForm(ModelForm):
    class Meta:
        model = Cause
        fields = ['label']
    label = CharField(widget=TextInput(attrs={}))
