from rest_framework import viewsets
from core.api.serializers import VeiculoSerializer
from core.models import Veiculo

class VeiculoViewset(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer