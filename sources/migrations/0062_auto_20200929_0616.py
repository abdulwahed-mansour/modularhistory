# Generated by Django 3.0.10 on 2020-09-29 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0061_auto_20200929_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcecontainment',
            name='container',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='container_containments', to='sources.Source'),
        ),
        migrations.AlterField(
            model_name='sourcecontainment',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_containments', to='sources.Source'),
        ),
    ]