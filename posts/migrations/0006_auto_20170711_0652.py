# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 06:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20170711_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
