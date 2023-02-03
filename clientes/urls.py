from django.urls import path
from clientes.views.cliente_views import *
from clientes.views.pedido_views import *

urlpatterns = [
    path('listar_clientes', listar_clientes, name='listar_clientes'),
    path('cadastrar_cliente', inserir_cliente, name='cadastrar_cliente'),
    path('listar_cliente/<int:id>', listar_cliente_id, name='listar_cliente_id'),
    path('editar_cliente/<int:id>', editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:id>', remover_cliente, name='remover_cliente'),
    path('cadastrar_pedido', inserir_pedido, name='cadastrar_pedido'),
]