# Generated by Django 4.2.6 on 2023-10-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acaiAplic', '0006_alter_itempedido_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('Finalizado', 'Finalizado'), ('Andamento', 'Andamento')]),
        ),
    ]