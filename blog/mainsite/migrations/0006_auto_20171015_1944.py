# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-10-15 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20171015_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_pic',
            name='article_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='article_tag',
            name='article_id',
            field=models.IntegerField(default=None),
        ),
    ]
