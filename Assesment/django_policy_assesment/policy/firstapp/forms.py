from .models import *
from django import forms 

class signForm(forms.ModelForm):
    class Meta:
        model=signup
        fields=['mail']


