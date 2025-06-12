from .models import Card
from django.forms import ModelForm
from django import forms

# declaring the ModelForm
class EditCardForm(ModelForm):
    
    class Meta:
        # the Model from which the form will inherit from
        model = Card
        # the fields we want from the Model
        fields = '__all__'
        # styling the form with bootstrap classes
        widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control'}),
             'description': forms.TextInput(attrs={'class': 'form-control'}),
             'associative_imagery': forms.TextInput(attrs={'class': 'form-control'}),
             'image': forms.FileInput(attrs={'class': 'form-control'}),
        }