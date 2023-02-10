from django import forms
from ..models import Pedido, Cliente, Produto

class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField( queryset=Cliente.objects.all() )
    produtos = forms.ModelMultipleChoiceField( queryset=Produto.objects.all() )
    class Meta:
        model = Pedido
        fields = ['cliente','observacoes', 'data_pedido', 'valor','status', 'produtos']
    