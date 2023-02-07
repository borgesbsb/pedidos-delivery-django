from django.urls import path
from clientes.views.cliente_views import *
from clientes.views.pedido_views import *
from clientes.views.produto_views import *

urlpatterns = [
    path('', listar_clientes, name='listar_clientes'),
    path('cadastrar_cliente', inserir_cliente, name='cadastrar_cliente'),
    path('listar_cliente/<int:id>', listar_cliente_id, name='listar_cliente_id'),
    path('editar_cliente/<int:id>', editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:id>', remover_cliente, name='remover_cliente'),
    path('cadastrar_pedido', inserir_pedido, name='cadastrar_pedido'),
    path('listar_pedidos', listar_pedidos, name='listar_pedidos'),
    path('editar_pedido/<int:id>', editar_pedido, name='editar_pedido'),
    path('listar_pedido/<int:id>', listar_pedido_id, name='listar_pedido_id'),
    path('cadastrar_produto', inserir_produto, name='cadastrar_produto'),
    path('listar_produtos', listar_produtos, name='listar_produtos'),
    path('listar_produto/<int:id>', listar_produto_id, name='listar_produto_id'),




]