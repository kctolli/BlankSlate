# Generated by Django 5.0 on 2023-12-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='response',
            field=models.CharField(choices=[('suffix', 'Suffix'), ('prefix', 'Prefix')], default='suffix', max_length=6),
        ),
    ]
