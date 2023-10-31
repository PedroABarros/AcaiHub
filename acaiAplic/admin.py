from django.contrib import admin

from acaiAplic.models import Cliente, pedido, itemPedido, Produto, endereco, endereco, formaDeEnvio, formaDePagamento

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome", "cpf", "numContato"]

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome_produto", "preco", "estoque")

@admin.register(endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("cidade", "cep", "logradouro", "bairro", "numero_casa", "complemento",  "pais", "uf", "endereco_cliente")

@admin.register(pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("data_pedido", "status", "cliente_pedido",)

@admin.register(itemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):

    list_display = ("produto", "quantidade", "pedido", "valorPedido")
    readonly_fields = ('valorPedido',)

@admin.register(formaDeEnvio)
class formaDeEnvioAdmin(admin.ModelAdmin):

    list_display = ("nome", "forma_envio")

@admin.register(formaDePagamento)
class formaDePagamentoAdmin(admin.ModelAdmin):

    list_display = ("nome", "forma_pagamento", "descricao", "numCartao")