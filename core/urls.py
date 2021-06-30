from core import views
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import VeiculoViewset

# Rest Framework
router = routers.DefaultRouter()
router.register(r'veiculos', VeiculoViewset)

urlpatterns = [
    path('', views.home, name='home'),
    path('detalhes/<int:veiculo_id>/', views.detalhes, name='detalhes'),
    path('comprar/', views.comprar, name='comprar'),
    path('vender/<int:veiculo_id>/', views.vender, name='vender'),
    path('resumo/', views.resumo, name='resumo'),
    path('disponiveis/', views.disponiveis, name='disponiveis'),
    path('vendidos/', views.vendidos, name='vendidos'),
    path('api-auth/', include('rest_framework.urls'), name='api'),
    path('api/', include(router.urls), name='api_veiculo'),
    path('sobre/', views.sobre, name='sobre')
]
