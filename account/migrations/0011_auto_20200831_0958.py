# Generated by Django 3.0.7 on 2020-08-31 09:58

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200831_0504'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
    ]
