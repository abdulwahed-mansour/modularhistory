# Generated by Django 3.0.5 on 2020-04-19 09:03

from django.db import migrations
import history.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0014_auto_20200329_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='bite',
            field=history.fields.HTMLField(blank=True, null=True, verbose_name='Bite'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='context',
            field=history.fields.HTMLField(blank=True, help_text='Content to be displayed after the quote', null=True, verbose_name='Context'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='pretext',
            field=history.fields.HTMLField(blank=True, help_text='Content to be displayed before the quote', null=True, verbose_name='Pretext'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='text',
            field=history.fields.HTMLField(verbose_name='Text'),
        ),
    ]