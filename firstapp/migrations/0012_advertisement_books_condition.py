# Generated by Django 3.2 on 2021-06-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_remove_advertisement_books_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='Books_Condition',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
