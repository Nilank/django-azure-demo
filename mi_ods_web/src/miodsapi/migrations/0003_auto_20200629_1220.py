# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-29 16:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miodsapi', '0002_auto_20200629_1212'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Meta_Study_Table_Config',
        ),
        migrations.DeleteModel(
            name='Meta_Table_Column_List',
        ),
        migrations.DeleteModel(
            name='Meta_Table_List',
        ),
    ]