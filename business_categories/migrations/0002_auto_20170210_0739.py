# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('business_categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bcategory',
            name='background_color',
            field=models.CharField(verbose_name='Background and Title Color', help_text='Ex: #FF0000', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bcategory',
            name='category_icon',
            field=models.CharField(help_text='Ex: fa fa-car', unique=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bsubcategory',
            name='sub_category',
            field=models.CharField(verbose_name='Sub Category', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bsubcategorytype',
            name='sub_category',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='category', to='business_categories.BSubCategory', chained_field='category', auto_choose=True, null=True),
        ),
        migrations.AlterField(
            model_name='bsubcategorytype',
            name='subcat_type',
            field=models.CharField(verbose_name='Sub Category Type', max_length=255, null=True),
        ),
    ]
