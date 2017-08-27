# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 15:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_lesson_bank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prize',
            options={'ordering': ['name'], 'verbose_name': 'приз', 'verbose_name_plural': 'призы'},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='bank',
            field=models.ForeignKey(blank=True, help_text='С кого списываются баллы за автонаграды', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prize',
            name='name',
            field=models.CharField(db_index=True, max_length=128, verbose_name='Название'),
        ),
    ]