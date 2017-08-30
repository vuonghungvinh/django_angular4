# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('category', models.CharField(unique=True, null=True, max_length=255, blank=True)),
                ('cat_logo', models.ImageField(upload_to='', height_field='height_field_logo', null=True, width_field='width_field_logo', verbose_name='Category Logo', blank=True)),
                ('height_field_logo', models.IntegerField(default=0)),
                ('width_field_logo', models.IntegerField(default=0)),
                ('cat_img', models.ImageField(upload_to='', height_field='height_field_img', null=True, width_field='width_field_img', verbose_name='Category Image', blank=True)),
                ('height_field_img', models.IntegerField(default=0)),
                ('width_field_img', models.IntegerField(default=0)),
                ('background_color', models.CharField(help_text='Ex: #FF0000', null=True, max_length=255, blank=True)),
                ('category_icon', models.CharField(unique=True, help_text='Ex: fa fa-mobile', null=True, max_length=255, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('cat_type', models.CharField(verbose_name='Category Type', null=True, max_length=255, blank=True)),
                ('cat_order', models.CharField(choices=[('1', 'Left'), ('2', 'Right')], verbose_name='Category Order', null=True, max_length=255, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classified_categories.Category')),
            ],
            options={
                'verbose_name': 'Category Type',
                'verbose_name_plural': 'Category Types',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('sub_category', models.CharField(verbose_name='Sub Category', null=True, max_length=255, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('cat_type', smart_selects.db_fields.ChainedForeignKey(chained_field='category', null=True, chained_model_field='category', verbose_name='Category Type', to='classified_categories.CategoryType', auto_choose=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classified_categories.Category')),
            ],
            options={
                'verbose_name': 'Sub Category',
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategoryType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('subcat_type', models.CharField(verbose_name='Sub Category Type', null=True, max_length=255, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('cat_type', smart_selects.db_fields.ChainedForeignKey(chained_field='category', null=True, chained_model_field='category', verbose_name='Category Type', to='classified_categories.CategoryType', auto_choose=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classified_categories.Category')),
                ('sub_category', smart_selects.db_fields.ChainedForeignKey(chained_field='cat_type', null=True, chained_model_field='cat_type', verbose_name='Sub Category', to='classified_categories.SubCategory', auto_choose=True)),
            ],
            options={
                'verbose_name': 'Sub Category Type',
                'verbose_name_plural': 'Sub Category Types',
            },
        ),
        migrations.AlterUniqueTogether(
            name='subcategorytype',
            unique_together=set([('category', 'sub_category', 'subcat_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='subcategory',
            unique_together=set([('category', 'sub_category')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytype',
            unique_together=set([('category', 'cat_type', 'cat_order')]),
        ),
    ]
