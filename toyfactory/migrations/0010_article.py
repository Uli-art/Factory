# Generated by Django 4.2.1 on 2023-09-22 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toyfactory', '0009_alter_review_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Text')),
                ('summary', models.CharField(max_length=100, verbose_name='Text')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Release Date')),
                ('text', models.CharField(max_length=1000, verbose_name='Text')),
                ('image', models.CharField(max_length=500, verbose_name='Text')),
            ],
        ),
    ]
