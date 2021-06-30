from django.shortcuts import redirect, render
from core.forms import *
from core.models import *
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
import datetime



def home(request):
    veiculos = Veiculo.objects.order_by("-data_compra").all()
    return render(request, 'home.html', {'veiculos': veiculos})


@login_required
def detalhes(request, veiculo_id):
    veiculo = Veiculo.objects.get(pk=veiculo_id)
    return render(request, 'detalhes.html', {'veiculo': veiculo})


@login_required
def comprar(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(home)
        messages.warning(request, 'Houve um erro!')
        return render(request, 'comprar.html', {'form': form})

    form = VeiculoForm()
    return render(request, 'comprar.html', {'form': form})




@login_required
def vender(request, veiculo_id):
    veiculo = Veiculo.objects.get(pk=veiculo_id)
    if request.method == 'POST':
        form = VendaForm(request.POST)

        if form.is_valid():
            form.save()

            carro = Veiculo.objects.get(pk=int(request.POST.get('carro')))
            carro.status = 'Vendido'
            carro.save()

            return redirect(home)

    form = VendaForm()
    return render(request, 'vender.html', {'form': form, 'veiculo': veiculo})


@login_required
def resumo(request):
    veiculo = Veiculo.objects.order_by("-data_compra").all()
    vendas = Venda.objects.order_by("-data_venda").all()

    lucro = Venda.objects.filter(status='Vender').aggregate(
        lucro=Sum('lucro')).get('lucro')

    gasto = Veiculo.objects.aggregate(valor=Sum('valor')).get('valor')
    ganho = Venda.objects.filter(status='Vender').aggregate(
        valor_venda=Sum('valor_venda')).get('valor_venda')

    comissoes = Venda.objects.filter(status='Vender').aggregate(
        comisao=Sum('comisao')).get('comisao')

    return render(request, 'resumo.html', {'vendas': vendas, 'receita': lucro, 'compras': veiculo, 'gasto': gasto, 'ganho': ganho, 'comisao':comissoes})


@login_required
def disponiveis(request):
    veiculos = Veiculo.objects.filter(status='Disponível').all()
    return render(request, 'disponiveis.html', {'veiculos': veiculos})


@login_required
def vendidos(request):

    vendas = Venda.objects.filter(status='Vender').all()
    return render(request, 'vendidos.html', {'vendas': vendas})

def sobre(request):
    return render(request, 'sobre.html')


