# Generated by Django 4.2.1 on 2023-09-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toyfactory', '0011_alter_article_image_alter_article_summary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
    ]
