# Generated by Django 3.0.4 on 2020-03-26 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_auto_20200326_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='parent_topics',
        ),
    ]
