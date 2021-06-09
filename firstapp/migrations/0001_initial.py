# Generated by Django 3.2 on 2021-05-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=250)),
                ('Authors_Name', models.CharField(max_length=250)),
                ('Category', models.CharField(max_length=250)),
                ('Books_Condition', models.BooleanField(default=False)),
                ('Location', models.CharField(max_length=250)),
                ('Details', models.TextField()),
                ('Price', models.IntegerField()),
                ('Image', models.CharField(max_length=250)),
            ],
        ),
    ]
