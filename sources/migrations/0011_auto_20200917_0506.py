# Generated by Django 3.0.7 on 2020-09-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0010_auto_20200917_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractPiece',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.textualsource',),
        ),
        migrations.AddField(
            model_name='typedsource',
            name='end_page_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='typedsource',
            name='page_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='typedsource',
            name='type',
            field=models.CharField(choices=[('sources.textualsource', 'textual source'), ('sources.abstractpiece', 'abstract piece')], db_index=True, max_length=255),
        ),
    ]