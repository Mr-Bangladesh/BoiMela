# Generated by Django 3.2 on 2021-06-05 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_auto_20210605_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='Books_Condition',
        ),
    ]