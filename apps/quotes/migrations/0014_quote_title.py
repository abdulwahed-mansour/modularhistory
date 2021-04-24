# Generated by Django 3.1.8 on 2021-04-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0013_auto_20210421_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='title',
            field=models.CharField(
                blank=True,
                help_text='The title can be used for the detail page header and title tag, SERP result card header, etc.',
                max_length=120,
                null=True,
                verbose_name='title',
            ),
        ),
    ]