# Generated by Django 5.0 on 2023-12-30 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0009_alter_word_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 8, 57, 51, 580507, tzinfo=datetime.timezone.utc)),
        ),
    ]
