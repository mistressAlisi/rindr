from django.forms import ModelForm,CharField,TextInput
from .models import Type

class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = ['label']
    label = CharField(widget=TextInput(attrs={}))
