from ..models import Produto

def inserir_produto(produto):
    Produto.objects.create( nome=produto.nome, 
                           descricao=produto.descricao,
                           valor=produto.valor )

def listar_produtos():
    produtos = Produto.objects.all()
    return produtos

def listar_produto_id(id):
    pedido = Produto.objects.get(id=id)
    return pedido