# Generated by Django 3.1.2 on 2020-10-31 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20201020_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotebite',
            name='computations',
        ),
    ]