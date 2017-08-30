# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170118_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adimage',
            name='image',
            field=models.ImageField(upload_to='', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='adname',
            name='ad_description',
            field=models.TextField(verbose_name='Ad Description', blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='adname',
            name='ad_title',
            field=models.CharField(verbose_name='Ad Title', blank=True, max_length=255, null=True),
        ),
    ]
