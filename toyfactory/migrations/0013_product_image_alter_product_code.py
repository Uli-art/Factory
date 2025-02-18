# Generated by Django 4.2.5 on 2023-10-07 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toyfactory', '0012_alter_article_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='/static/toyfactory/images/products/default.png', max_length=500, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.PositiveIntegerField(default=0, unique=True, verbose_name='Code'),
        ),
    ]
