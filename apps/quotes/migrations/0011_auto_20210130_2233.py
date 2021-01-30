# Generated by Django 3.1.5 on 2021-01-30 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_auto_20201216_0032'),
        ('quotes', '0010_auto_20201208_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='quote_relations', to='images.image', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='quoteimage',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_relations', to='quotes.quote', verbose_name='quote'),
        ),
    ]
