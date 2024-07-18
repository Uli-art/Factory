# Generated by Django 4.2.1 on 2023-06-02 10:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+375(29)XXX-XX-XX'", regex='^+375(29)ddd-dd-dd$')], verbose_name='Phone Number')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Price')),
                ('out_of_production', models.BooleanField(default=False, verbose_name='Out Of Production')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toyfactory.productmodel')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toyfactory.producttype')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Order Date')),
                ('completion_date', models.DateTimeField(verbose_name='Completion Date')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toyfactory.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toyfactory.product')),
            ],
        ),
    ]
