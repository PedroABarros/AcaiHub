# Generated by Django 4.2.6 on 2023-10-18 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acaiAplic', '0008_formadepagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='formadepagamento',
            name='descricao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acaiAplic.produto'),
        ),
    ]
