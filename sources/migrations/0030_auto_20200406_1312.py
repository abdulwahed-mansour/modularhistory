# Generated by Django 3.0.4 on 2020-04-06 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0029_auto_20200406_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qsr',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='qsr',
            name='source',
        ),
        migrations.DeleteModel(
            name='OSR',
        ),
        migrations.DeleteModel(
            name='QSR',
        ),
    ]