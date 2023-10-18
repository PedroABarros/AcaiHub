# Generated by Django 4.2.6 on 2023-10-18 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='cpf')),
                ('numContato', models.CharField(max_length=15, verbose_name='Numero Contato')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=50, unique=True, verbose_name='Nome do Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Estoque')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(verbose_name='Horario do Pedido')),
                ('status', models.CharField(choices=[('Feito', 'Feito'), ('Finalizado', 'Finalizado'), ('Andamento', 'Andamento')])),
                ('cliente_pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acaiAplic.cliente')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='itemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade Pedida')),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acaiAplic.pedido')),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acaiAplic.produto')),
            ],
            options={
                'verbose_name': 'Item Pedido',
                'verbose_name_plural': 'Items Pedido',
            },
        ),
        migrations.CreateModel(
            name='formaDeEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_envio', models.CharField(choices=[('motoboy', 'Motoboy'), ('retirada_local', 'Retirada no Local')], default='motoboy', max_length=15)),
                ('prazo_entrega', models.PositiveIntegerField()),
                ('custo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acaiAplic.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=200, verbose_name='Logradouro')),
                ('complemento', models.CharField(max_length=200, verbose_name='Complemento')),
                ('numero_casa', models.CharField(max_length=6, verbose_name='Número ')),
                ('bairro', models.CharField(max_length=200, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('pais', models.CharField(max_length=200, verbose_name='Pais')),
                ('uf', models.CharField(default=None, max_length=200, verbose_name='UF')),
                ('endereco_cliente', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='acaiAplic.cliente')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]