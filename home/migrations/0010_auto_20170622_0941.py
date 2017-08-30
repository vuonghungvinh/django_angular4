# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_countryinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adimage',
            name='adname_id',
        ),
        migrations.AddField(
            model_name='adimage',
            name='adname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adimages', to='home.AdName'),
        ),
        migrations.AlterField(
            model_name='countryinfo',
            name='country',
            field=models.IntegerField(choices=[(1, 'UAE'), (2, 'Egypt'), (3, 'Bahrain'), (4, 'KSA'), (5, 'Lebanon'), (6, 'Kuwait'), (7, 'Oman'), (8, 'Qatar')], default=0),
        ),
    ]
