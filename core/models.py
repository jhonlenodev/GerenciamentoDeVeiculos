from django.db import models
from django.contrib.auth.models import User


class Veiculo(models.Model):

    STATUS_CHOICES = (
        ('Disponível', 'Disponível'),
        ('Vendido', 'Vendido'),
    )

    modelo = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10, unique=True)
    cor = models.CharField(max_length=100)
    chassi = models.CharField(max_length=50, unique=True)
    data_compra = models.DateTimeField(auto_now_add=True)
    valor = models.FloatField()
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='Disponivel')

    def __str__(self):
        return self.modelo + ' - ' + self.placa

    class Meta:
        ordering = ['-data_compra']


class Venda(models.Model,):
    STATUS_CHOICES = (('Disponivel', 'Disponivel'), ('Vender', 'Vender'))

    carro = models.ForeignKey(Veiculo, blank=True, on_delete=models.PROTECT)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    valor_venda = models.FloatField()
    data_venda = models.DateTimeField(auto_now_add=True)
    comisao = models.FloatField()
    lucro = models.FloatField()
    comprador = models.CharField(max_length=100)
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='Vender')

    def __str__(self):
        return self.comprador

    class Meta:
        ordering = ['-data_venda']
