from django import forms
from .models import Mecanico

class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = '__all__'