# Generated by Django 3.0.4 on 2020-03-29 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occurrences', '0006_auto_20200329_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occurrence',
            old_name='sources',
            new_name='sources2',
        ),
    ]