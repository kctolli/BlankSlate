# Generated by Django 5.0 on 2023-12-27 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0007_alter_word_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 15, 51, 56, 868284, tzinfo=datetime.timezone.utc)),
        ),
    ]