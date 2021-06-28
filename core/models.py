from django.db import models

class Veiculo(models.Model):
    modelo = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10 , unique=True)
    cor = models.CharField(max_length=100)
    chassi = models.CharField(max_length=50, unique=True)
    data_compra = models.DateField(auto_now_add=True)
    valor = models.FloatField()
    
class Venda(models.Model):
    valor_venda = models.FloatField()
    data_compra = models.DateField(auto_now_add=True)
    comisao = models.FloatField()
    lucro = models.FloatField()