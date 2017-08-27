# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20170804_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='casinosession',
            name='won',
            field=models.IntegerField(default=0, verbose_name='Выигрыш'),
        ),
        migrations.AlterField(
            model_name='casinosession',
            name='start',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Начало сессии'),
        ),
    ]
