from django.db import models
from django.utils import timezone
from django.db.models.signals import m2m_changed

# Create your models here.
class Endereco(models.Model):
    
    PAIS_CHOICES = (
        ('BR', 'Brasil'),
        ('PT', 'Portugal'),
        ('FR', 'França')
    )
    
    rua = models.CharField(max_length=200, null=False, blank=False )
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    pais = models.CharField(max_length=2,choices=PAIS_CHOICES, null=False, blank=False)
    
    
    def __str__(str):
        return self.rua

class Produto(models.Model):
    nome = models.CharField(max_length=50,null=False,blank=False)
    descricao = models.CharField(max_length=100,null=False,blank=False)
    valor = models.FloatField(null=False, blank=False)
    
    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )
    cliente = models.ForeignKey( "Cliente", on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(default=timezone.now)
    valor = models.FloatField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False )
    observacoes = models.CharField(max_length=50, null=True, blank=True)
    produtos = models.ManyToManyField(Produto)
    
    def __str__(self):
        return self.cliente.nome


def pre_save_produto_receiver(sender, instance, action, **kwargs ):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        produtos = instance.produtos.all()
        total = 0
        for i in produtos:
            total += i.valor
        instance.valor = total
        instance.save()

m2m_changed.connect(pre_save_produto_receiver, sender=Pedido.produtos.through)
    


class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    
  
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome



    



