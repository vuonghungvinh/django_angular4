# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_adname_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adname',
            name='ad_type',
            field=models.IntegerField(default=0),
        ),
    ]
