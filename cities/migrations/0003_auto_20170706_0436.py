# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20170210_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(blank=True, choices=[('BH', 'Bahrain'), ('EG', 'Egypt'), ('KW', 'Kuwait'), ('LB', 'Lebanon'), ('OM', 'Oman'), ('QA', 'Qatar'), ('SA', 'Saudi Arabia'), ('AE', 'United Arab Emirates')], max_length=255, null=True),
        ),
    ]
