# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20161228_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='level',
            field=models.PositiveSmallIntegerField(default=1, editable=False, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='position',
            field=models.PositiveSmallIntegerField(default=1, editable=False, verbose_name='Позиция'),
        ),
    ]