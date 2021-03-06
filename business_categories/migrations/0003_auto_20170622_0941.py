# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('business_categories', '0002_auto_20170210_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bsubcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bsubcategories', to='business_categories.BCategory'),
        ),
        migrations.AlterField(
            model_name='bsubcategorytype',
            name='sub_category',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bsubcategorytypies', to='business_categories.BSubCategory'),
        ),
    ]
