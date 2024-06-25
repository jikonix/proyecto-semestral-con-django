from django import forms
from .models import Pizza

class nueva_pizza(forms.ModelForm):
    class Meta:
        model=  Pizza
        fields= "__all__"
