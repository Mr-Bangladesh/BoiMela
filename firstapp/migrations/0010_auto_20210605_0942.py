# Generated by Django 3.2 on 2021-06-05 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0009_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='District',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='Division',
        ),
    ]
