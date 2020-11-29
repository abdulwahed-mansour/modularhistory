# Generated by Django 3.1.3 on 2020-11-29 21:12

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0005_auto_20201129_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='get_slug', unique=True, verbose_name='slug'),
        ),
    ]
