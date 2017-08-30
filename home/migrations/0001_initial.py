# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import home.models
import geoposition.fields
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdFeatures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rand_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('usertype', models.CharField(max_length=255, null=True, blank=True)),
                ('condition_of_item', models.CharField(max_length=255, null=True, blank=True)),
                ('period_used', models.CharField(max_length=255, null=True, blank=True)),
                ('warranty', models.CharField(max_length=255, null=True, blank=True)),
                ('position', geoposition.fields.GeopositionField(max_length=42, null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdFeaturesPricing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True, countries=home.models.G8Countries)),
                ('price', models.CharField(max_length=255, null=True, blank=True)),
                ('currency', models.CharField(max_length=255, null=True, blank=True)),
                ('negotiable', models.IntegerField(default=0)),
                ('counter', models.IntegerField(default=0)),
                ('delivery_included', models.IntegerField(default=0)),
                ('delivery_comments', models.TextField(max_length=255, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('ad_features', models.ForeignKey(blank=True, to='home.AdFeatures', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rand_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('usertype', models.CharField(max_length=255, null=True, blank=True)),
                ('adname_id', models.IntegerField(default=0)),
                ('counter', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rand_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('usertype', models.CharField(max_length=255, null=True, blank=True)),
                ('ad_title', models.CharField(max_length=255, null=True, verbose_name=b'Ad Title', blank=True)),
                ('ad_description', models.TextField(max_length=255, null=True, verbose_name=b'Ad Description', blank=True)),
                ('cat_id', models.IntegerField(default=0)),
                ('sub_cat_id', models.IntegerField(default=0)),
                ('sub_type_id', models.IntegerField(default=0)),
                ('ad_complete_status', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdPricing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rand_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('usertype', models.CharField(max_length=255, null=True, blank=True)),
                ('ad_option', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
