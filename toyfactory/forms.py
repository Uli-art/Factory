from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class OrderSearchForm(forms.Form):
    customer = forms.CharField(label="Customer", max_length=255)
    product = forms.CharField(label="Product", max_length=255)


class ReviewForm(forms.Form):
    rating = forms.IntegerField(label="rating", validators=[
            MaxValueValidator(5),
            MinValueValidator(1)]
        )
    text = forms.CharField(label="text", max_length=500, required=False)


class ArticleForm(forms.Form):
    title = forms.CharField(label="title", max_length=100)
    summary = forms.CharField(label="summary", max_length=100)
    text = forms.CharField(label="text", max_length=1000)
    image = forms.CharField(label="image", max_length=500)


class CouponForm(forms.Form):
    title = forms.CharField(label="title", max_length=100)
    date = forms.DateField(label="release Date")
    description = forms.CharField(label="description")
    image = forms.CharField(label="image", max_length=500)
    promo_code = forms.CharField(label="promo code", max_length=15)
    discount = forms.IntegerField(label="discount")