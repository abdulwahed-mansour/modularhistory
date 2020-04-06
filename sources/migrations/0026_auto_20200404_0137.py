# Generated by Django 3.0.4 on 2020-04-04 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0025_auto_20200402_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='printing_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]