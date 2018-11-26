# Generated by Django 2.1.2 on 2018-11-21 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181120_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusvenda',
            name='hide',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='statusvenda',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Ordem'),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='dt_pedido',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 21, 9, 10, 18, 295536)),
        ),
    ]