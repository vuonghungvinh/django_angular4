# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=255, unique=True, null=True)),
                ('background_color', models.CharField(help_text=b'Ex: #FF0000', max_length=255, null=True, verbose_name=b'Background and Title Color')),
                ('category_icon', models.CharField(help_text=b'Ex: fa fa-car', max_length=255, unique=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='BSubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_category', models.CharField(max_length=255, null=True, verbose_name=b'Sub Category')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='business_categories.BCategory', null=True)),
            ],
            options={
                'verbose_name': 'Sub Category',
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='BSubCategoryType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcat_type', models.CharField(max_length=255, null=True, verbose_name=b'Sub Category Type')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='business_categories.BCategory', null=True)),
                ('sub_category', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'category', to='business_categories.BSubCategory', chained_field=b'category', null=True, auto_choose=True)),
            ],
            options={
                'verbose_name': 'Sub Category Type',
                'verbose_name_plural': 'Sub Category Types',
            },
        ),
        migrations.AlterUniqueTogether(
            name='bsubcategorytype',
            unique_together=set([('category', 'sub_category', 'subcat_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='bsubcategory',
            unique_together=set([('category', 'sub_category')]),
        ),
    ]
