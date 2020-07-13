# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-29 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miodsapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta_Study_Table_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=60)),
                ('merge_sp', models.CharField(max_length=60)),
                ('tims_schema', models.CharField(max_length=60)),
                ('schema_name', models.CharField(max_length=60)),
                ('cdc_date', models.DateTimeField(blank=True, null=True)),
                ('sql_data_extract', models.TextField()),
                ('is_enabled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'META_STUDY_TABLE_CONFIG',
            },
        ),
        migrations.CreateModel(
            name='Meta_Table_Column_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=60)),
                ('column_name', models.CharField(max_length=100)),
                ('sequence_number', models.IntegerField()),
                ('data_type', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'META_TABLE_COLUMN_LIST',
            },
        ),
        migrations.CreateModel(
            name='Meta_Table_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=60)),
                ('merge_sp', models.CharField(max_length=60)),
                ('is_enabled', models.BooleanField(default=True)),
                ('is_db_load_enabled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'META_TABLE_LIST',
            },
        ),
        migrations.AlterModelTable(
            name='meta_study_config',
            table='META_STUDY_CONFIG',
        ),
    ]
