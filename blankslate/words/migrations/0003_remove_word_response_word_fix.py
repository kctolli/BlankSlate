# Generated by Django 5.0 on 2023-12-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_word_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='response',
        ),
        migrations.AddField(
            model_name='word',
            name='fix',
            field=models.CharField(choices=[('suffix', 'Suffix'), ('prefix', 'Prefix')], default='prefix', max_length=6),
        ),
    ]