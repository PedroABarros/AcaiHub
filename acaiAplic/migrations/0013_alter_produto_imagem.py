# Generated by Django 4.2.6 on 2023-11-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acaiAplic', '0012_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/', verbose_name='Imagem'),
        ),
    ]
