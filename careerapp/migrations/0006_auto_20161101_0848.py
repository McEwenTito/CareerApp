# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-01 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerapp', '0005_careerpathway_cluster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careercluster',
            name='info',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]