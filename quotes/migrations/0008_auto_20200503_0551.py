# Generated by Django 3.0.5 on 2020-05-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0007_auto_20200430_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotebite',
            name='end',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quotebite',
            name='start',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]