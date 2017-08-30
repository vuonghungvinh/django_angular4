# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_adname_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='adname',
            name='ad_type',
            field=models.IntegerField(default=2),
        ),
    ]
