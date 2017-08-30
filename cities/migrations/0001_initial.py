# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cities.models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True, countries=cities.models.G8Countries)),
                ('city', models.CharField(max_length=255, null=True, verbose_name=b'City', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'cities',
                'verbose_name_plural': 'city list',
            },
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('country', 'city')]),
        ),
    ]
