# Generated by Django 3.1.9 on 2021-05-18 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0015_auto_20210518_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='source',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='_citations',
                to='sources.source',
            ),
        ),
    ]