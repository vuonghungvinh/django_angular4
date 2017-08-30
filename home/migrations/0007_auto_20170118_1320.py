# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170109_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adpricing',
            old_name='ad_option',
            new_name='ad_featured',
        ),
        migrations.AddField(
            model_name='adpricing',
            name='ad_premium',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adpricing',
            name='ad_push_to_top',
            field=models.IntegerField(default=0),
        ),
    ]
