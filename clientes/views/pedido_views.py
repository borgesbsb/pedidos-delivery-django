from django.shortcuts import render
from ..forms import pedido_forms
from ..entidades import pedido
from ..services import pedido_service


def inserir_pedido(request):
    if request.method == "POST":
        form_pedido = pedido_forms.PedidoForm(request.POST)
        if form_pedido.is_valid():
            cliente = form_pedido.cleaned_data["cliente"]
            observacoes = form_pedido.cleaned_data["observacoes"]
            valor = form_pedido.cleaned_data["valor"]
            status = form_pedido.cleaned_data["status"]
            data_pedido = form_pedido.cleaned_data["data_pedido"]
            pedido_novo = pedido.Pedido( cliente=cliente,
                                        observacoes=observacoes, 
                                        valor=valor,
                                        status=status,
                                        data_pedido=data_pedido 
                                        )
            pedido_service.cadastrar_pedido(pedido_novo)
    else:
        form_pedido = pedido_forms.PedidoForm()
    return render(request, 'pedidos/form_pedido.html', {'form_pedido': form_pedido})
