# Generated by Django 3.1.3 on 2020-11-18 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_remove_image_cropping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='verified'),
        ),
        migrations.AlterField(
            model_name='video',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='verified'),
        ),
    ]