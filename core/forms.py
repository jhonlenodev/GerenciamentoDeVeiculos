from django import forms
from core.models import *

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
        
class VendaForm(forms.ModelForm):
    carro = forms.ModelChoiceField(queryset=Veiculo.objects.filter(status='Disponível'))
    class Meta:
        model = Venda
        fields = '__all__'