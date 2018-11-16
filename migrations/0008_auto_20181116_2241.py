# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-16 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery657', '0007_auto_20180906_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AddField(
            model_name='collection',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
