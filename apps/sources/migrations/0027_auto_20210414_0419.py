# Generated by Django 3.1.8 on 2021-04-14 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0026_auto_20210414_0414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sourceattribution',
            old_name='source',
            new_name='old_source',
        ),
    ]