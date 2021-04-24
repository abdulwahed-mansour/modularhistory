# Generated by Django 3.1.8 on 2021-04-21 02:55

from django.db import migrations

import core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('postulations', '0006_postulation_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulation',
            name='notes',
            field=core.fields.HTMLField(
                blank=True, null=True, paragraphed=True, processed=False, processor=None
            ),
        ),
        migrations.AlterField(
            model_name='postulation',
            name='summary',
            field=core.fields.HTMLField(
                paragraphed=False,
                processed=False,
                processor=None,
                unique=True,
                verbose_name='statement',
            ),
        ),
    ]