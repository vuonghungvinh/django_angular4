# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='conversion_rate',
            field=models.FloatField(verbose_name='Conversion Rate', blank=True, max_length=255, null=True),
        ),
    ]
