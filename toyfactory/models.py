from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import datetime
from threading import local


class ProductType(models.Model):
    name = models.CharField("Name", max_length=255)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField("Name", max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.PositiveIntegerField("Code", unique=True, default=0)
    name = models.CharField("Name", max_length=255)
    type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    model = models.ForeignKey(ProductModel, on_delete=models.PROTECT)
    price = models.PositiveIntegerField("Price", default=0)
    image = models.CharField("Image", max_length=500, default="/static/toyfactory/images/products/default.png")
    in_production = models.BooleanField("In Production", default=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    code = models.PositiveIntegerField("Code", unique=True)
    name = models.CharField("Name", max_length=255)
    phone_regex = RegexValidator(regex=r'\+375\(29\)\d{3}-\d{2}-\d{2}',
                                 message="Phone number must be entered in the format: '+375(29)XXX-XX-XX'")
    phone = models.CharField("Phone Number", validators=[phone_regex], max_length=20, blank=True)
    city = models.CharField("City", max_length=255)
    address = models.CharField("Address", max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateField("Order Date")
    completion_date = models.DateField("Completion Date", blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField("Quantity")
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.date) + " - [" + str(self.id) + "] " + self.customer.name


class Review(models.Model):
    clients_name = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField("Rating", validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    date = models.DateField("Release Date", default=datetime.date.today)
    text = models.CharField("Text", max_length=500, null=True)


class Article(models.Model):
    title = models.CharField("Title", max_length=100)
    summary = models.CharField("Summary", max_length=500)
    date = models.DateField("Release Date", default=datetime.date.today)
    text = models.TextField("Text")
    image = models.CharField("Image", max_length=500)


class Coupon(models.Model):
    title = models.CharField("Title", max_length=100)
    date = models.DateField("Release Date", null=True)
    description = models.TextField("Description")
    image = models.CharField("Image", max_length=500)
    promo_code = models.TextField("Promo code", max_length=100, null=True)
    discount = models.PositiveIntegerField("Discount", default=0)
