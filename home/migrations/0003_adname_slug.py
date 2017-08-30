# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20161124_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='adname',
            name='slug',
            field=models.SlugField(max_length=255, null=True, blank=True),
        ),
    ]
