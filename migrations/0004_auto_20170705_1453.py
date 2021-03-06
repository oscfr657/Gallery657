# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery657', '0003_auto_20170423_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mediafile',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_file', related_query_name='media_files', to='gallery657.Collection'),
        ),
    ]
