# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 07:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170807_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='bank',
            field=models.ForeignKey(help_text='С кого списываются баллы за автонаграды', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
