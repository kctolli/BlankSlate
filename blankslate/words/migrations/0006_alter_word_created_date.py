# Generated by Django 5.0 on 2023-12-27 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_alter_word_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 14, 52, 17, 281523, tzinfo=datetime.timezone.utc)),
        ),
    ]
