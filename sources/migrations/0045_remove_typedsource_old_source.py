# Generated by Django 3.0.7 on 2020-09-24 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0044_auto_20200924_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typedsource',
            name='old_source',
        ),
    ]