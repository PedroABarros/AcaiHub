from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(_("Nome"), blank=False, max_length=50,)
    cpf = models.CharField(_("cpf"), blank=False, max_length=11, unique=True)
    numContato = models.CharField(_("Numero Contato"), blank=False, max_length=15)

    class Meta:    
        abstract = True
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoas')
        ordering = ['id']

        def __str__(self):
            return self.nome
        

        
class Cliente(Pessoa):
    email = models.EmailField()


    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')



class produto(models.Model):
    nome_produto =  models.CharField(_("Nome do Produto"), blank=False, max_length=50, unique=True,)
    preco = models.DecimalField(_("Preço"), null=True, blank=False, max_digits=8, decimal_places=2)
    estoque = models.IntegerField(_('Estoque'))
    

    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def __str__(self):
        return f"{self.nome_produto} / R${self.preco}"
    


class pedido(models.Model):

    data_pedido = models.DateTimeField(_('Horario do Pedido'), blank=False)
    status = models.DecimalField(_("Carga horária"), null=True,blank=False, max_digits=12, decimal_places=3)
    cliente_pedido = models.ForeignKey(Cliente, blank=False, null=True, on_delete= models.SET_NULL)
    FEITO = "Feito"
    FINALIZADO = "Finalizado"
    ANDAMENTO = "Andamento"

    CHOICES = [
        (FEITO, "Feito"),
        (FINALIZADO,"Finalizado"),
        (ANDAMENTO,"Andamento"),
    
    ]
    status = models.CharField(
        choices=CHOICES,
    )

    class Meta:
        verbose_name = _('Pedido')
        verbose_name_plural = _('Pedidos')

    def __str__(self):
        return f"{self.data_pedido} / {self.status}"
    


    
class itemPedido(models.Model):
    produto = models.ForeignKey(produto, blank=True, null=True, on_delete= models.SET_NULL)
    quantidade = models.IntegerField(_("Quantidade Pedida"))
    pedido = models.ForeignKey(pedido , blank=True, null=True, on_delete= models.SET_NULL)
    

    def valorPedido(self):
        return self.quantidade * self.produto.preco

    class Meta:
        verbose_name = _('Item Pedido')
        verbose_name_plural = _('Items Pedido')

    def __str__(self):
        return f"Produto {self.produto} / Quantidade: {self.quantidade}"
    


    
class endereco(models.Model):
    
    cep = models.CharField(_('CEP'),)
    logradouro = models.CharField(_('Logradouro'), max_length=200)
    complemento = models.CharField(_('Complemento'), max_length=200)
    numero_casa = models.CharField(_('Número '),)
    bairro = models.CharField(_('Bairro'), max_length=200)
    cidade = models.CharField(_('Cidade'), max_length=200)
    pais = models.CharField(_('Pais'), max_length=200)
    uf = models.CharField(_('UF'), max_length=200, blank=False, default=None)
    endereco_cliente = models.ForeignKey(Cliente, blank=True, default=None, null=True, on_delete= models.DO_NOTHING)
    
    class Meta:
            verbose_name = _('Endereço')
            verbose_name_plural = _('Endereços')

        
    def __str__(self):
        return f"Cidade: {self.cidade} | Bairro: {self.bairro} | Rua: {self.logradouro}"
    

    
    
class formaDeEnvio(models.Model):

    FORMA_ENVIO_CHOICES = [
        ('motoboy', 'Motoboy'),
        ('retirada_local', 'Retirada no Local'),
    ]

    nome = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    forma_envio = models.CharField(
        max_length=15,
        choices=FORMA_ENVIO_CHOICES,
        default='motoboy'
    )
    prazo_entrega = models.PositiveIntegerField()
    custo = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.get_forma_envio_display()} - Entrega em {self.prazo_entrega} dias - Custo: {self.custo} BRL"

    

