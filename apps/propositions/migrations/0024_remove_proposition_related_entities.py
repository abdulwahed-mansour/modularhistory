# Generated by Django 3.1.13 on 2021-08-23 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propositions', '0023_auto_20210823_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposition',
            name='related_entities',
        ),
    ]
