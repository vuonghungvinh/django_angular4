# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_adname_ad_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='adname',
            name='category_type',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
