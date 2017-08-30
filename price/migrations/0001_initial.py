# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
import price.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True, countries=price.models.G8Countries)),
                ('to_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True, countries=price.models.G8Countries)),
                ('conversion_rate', models.FloatField(max_length=255, null=True, verbose_name=b'Conversion Rate', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'price',
                'verbose_name_plural': 'price list',
            },
        ),
        migrations.AlterUniqueTogether(
            name='price',
            unique_together=set([('from_country', 'to_country', 'conversion_rate')]),
        ),
    ]
