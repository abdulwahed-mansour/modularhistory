# Generated by Django 3.0.4 on 2020-03-29 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0011_auto_20200328_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotesourcereference',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citations2', to='quotes.Quote'),
        ),
    ]
