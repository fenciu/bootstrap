# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-10-15 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20171012_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='article',
            name='article_pic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainsite.article_pic'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_tag',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainsite.article_tag'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
