# Generated by Django 4.2.1 on 2023-06-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toyfactory', '0004_alter_order_completion_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='completion_date',
            field=models.DateField(blank=True, null=True, verbose_name='Completion Date'),
        ),
    ]
