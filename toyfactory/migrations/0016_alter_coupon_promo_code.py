# Generated by Django 4.2.5 on 2023-11-18 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toyfactory', '0015_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='promo_code',
            field=models.TextField(max_length=100, null=True, verbose_name='Promo code'),
        ),
    ]
