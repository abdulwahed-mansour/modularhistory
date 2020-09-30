# Generated by Django 3.0.7 on 2020-09-21 08:16

from django.db import migrations, models
import django.db.models.deletion
import history.fields.json_field


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0017_auto_20200917_1445'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TitledSource',
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sources.sourcewithpagenumbers',),
        ),
        migrations.AlterModelOptions(
            name='typedsource',
            options={'ordering': ['creators', '-date']},
        ),
        migrations.RemoveField(
            model_name='typedsource',
            name='editors',
        ),
        migrations.RemoveField(
            model_name='typedsource',
            name='end_page_number',
        ),
        migrations.RemoveField(
            model_name='typedsource',
            name='page_number',
        ),
        migrations.AddField(
            model_name='typedsource',
            name='extra',
            field=history.fields.json_field.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='typedsource',
            name='publication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sources.Publication'),
        ),
        migrations.AlterField(
            model_name='typedsource',
            name='type',
            field=models.CharField(choices=[('sources.textualsource', 'textual source'), ('sources.sourcewithpagenumbers', 'source with page numbers'), ('sources.article', 'article')], db_index=True, max_length=255),
        ),
    ]