from django.shortcuts import render
from core.models import *

def home(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'home.html', {'veiculos':veiculos})
