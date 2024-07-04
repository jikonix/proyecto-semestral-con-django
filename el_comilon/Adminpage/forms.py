from django import forms
from .models import Comidas

class Nuevo_item(forms.ModelForm):
    class Meta:
        model= Comidas
        fields= "__all__"
        exclude= ["fecha_ingreso", "slug"]
