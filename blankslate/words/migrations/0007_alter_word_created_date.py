# Generated by Django 5.0 on 2023-12-27 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0006_alter_word_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 15, 29, 51, 284609, tzinfo=datetime.timezone.utc)),
        ),
    ]