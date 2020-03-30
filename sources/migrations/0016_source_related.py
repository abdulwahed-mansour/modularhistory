# Generated by Django 3.0.4 on 2020-03-29 11:00

from django.db import migrations
import gm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('sources', '0015_auto_20200329_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='related',
            field=gm2m.fields.GM2MField(blank=True, related_name='sources', through='sources.Citation', through_fields=['source', 'content_object', 'content_type', 'object_id']),
        ),
    ]