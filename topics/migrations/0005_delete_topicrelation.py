# Generated by Django 3.0.5 on 2020-04-30 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_auto_20200430_0031'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TopicRelation',
        ),
    ]