from django.db import models

class Veiculo(models.Model):
    modelo = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    
    data_compra = models.DateField(auto_now_add=True)
    