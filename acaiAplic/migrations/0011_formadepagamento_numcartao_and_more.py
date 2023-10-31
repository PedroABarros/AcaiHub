# Generated by Django 4.2.6 on 2023-10-18 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acaiAplic', '0010_alter_formadepagamento_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='formadepagamento',
            name='numCartao',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Número do Cartão'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='endereco_cliente',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acaiAplic.cliente'),
        ),
    ]