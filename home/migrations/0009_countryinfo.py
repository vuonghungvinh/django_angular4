# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170210_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.IntegerField(default=0)),
                ('country_name', models.CharField(null=True, blank=True, max_length=255)),
                ('currency', models.CharField(null=True, blank=True, max_length=255)),
            ],
        ),
    ]
