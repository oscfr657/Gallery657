# Generated by Django 2.2.1 on 2019-08-24 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery657', '0012_auto_20190625_2201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'Works of art'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'Collections'},
        ),
    ]