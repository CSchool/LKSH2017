# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 22:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170801_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='code',
            field=models.CharField(max_length=8, unique=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='prize',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='main.Prize'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('PD', 'Оплачено'), ('RC', 'Получено'), ('DC', 'Отклонено'), ('RF', 'Возвращено')], default='PD', max_length=2, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL),
        ),
    ]
