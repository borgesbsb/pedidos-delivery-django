from clientes.forms.produto_forms import ProdutoForm
from django.shortcuts import render, redirect
from ..entidades.produto import Produto
from ..services import produto_service

def inserir_produto (request):
    if request.method == 'POST':
        form_produto = ProdutoForm(request.POST)
        if form_produto.is_valid():
            nome = form_produto.cleaned_data['nome']
            descricao = form_produto.cleaned_data['descricao']
            valor = form_produto.cleaned_data['valor']
            produto_novo = Produto(nome=nome,descricao=descricao,valor=valor)
            produto_service.inserir_produto(produto_novo)
            return redirect('listar_produtos')
    form_produto  = ProdutoForm()
    return render(request,'produtos/form_produto.html', {'form_produto': form_produto })
    
def listar_produtos(request):
    produtos = produto_service.listar_produtos()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def listar_produto_id(request, id):
    produto = produto_service.listar_produto_id(id)
    return render(request, 'produtos/lista_produto.html',{"produto":produto})
