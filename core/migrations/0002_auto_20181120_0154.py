# Generated by Django 2.0.4 on 2018-11-20 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='tipopessoa',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cliente',
            field=models.BooleanField(default=0, verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='fornecedor',
            field=models.BooleanField(default=0, verbose_name='Fornecedor'),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='dt_pedido',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 20, 1, 54, 41, 314482)),
        ),
    ]
