# Generated by Django 2.2.1 on 2019-06-25 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery657', '0011_auto_20190511_2240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art',
            options={'ordering': ['-pub_date']},
        ),
    ]
