# Generated by Django 5.0 on 2023-12-30 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0010_alter_word_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='created_date',
        ),
    ]
