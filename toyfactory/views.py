from django.core import serializers
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView, TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Sum, Count

import pandas as pd
import django_filters
import logging

from .models import Order, ProductType, Product, Customer, Review, Article, Coupon
from .forms import OrderSearchForm, ReviewForm, ArticleForm
from .api import CouponSerializer

def index(request):
    return render(request, "toyfactory/index.html")


class AdditionalView(TemplateView):
    template_name = "toyfactory/additional.html"


class AboutUsView(TemplateView):
    template_name = "toyfactory/about_us.html"


class PrivacyPolicyView(TemplateView):
    template_name = "toyfactory/privacy_policy.html"


class ContactsView(TemplateView):
    template_name = "toyfactory/contacts.html"


class VacanciesView(TemplateView):
    template_name = "toyfactory/vacancies.html"


class CouponsView(TemplateView):
    template_name = "toyfactory/coupons.html"
    model = Coupon

    def  get_queryset(self):
        return Coupon.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coupons"] = Coupon.objects.all()
        return context


class QuestionsView(TemplateView):
    template_name = "toyfactory/questions.html"
    model = Product

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        tmp1 = []
        for i in range(0, 4):
            tmp1.append(products[i])
        context["products_list1"] = tmp1
        tmp2 = []
        for i in range(1, 5):
            tmp2.append(products[i])
        context["products_list2"] = tmp2
        return context


class ArticleView(TemplateView):
    template_name = "toyfactory/article.html"
    model = Article

    def get_queryset(self):
        if "news_id" not in self.kwargs:
            self.news_id = None
            return Article.objects.all()

        self.news_id = get_object_or_404(1, id=self.kwargs["news_id"])
        return Article.objects.filter(id=self.news_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "news_id" not in self.kwargs:
            return context
        context["article"] = Article.objects.filter(id=self.kwargs["news_id"])
        return context


class NewsView(TemplateView):
    template_name = "toyfactory/news.html"

    def get_queryset(self):
        return Article.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_list"] = Article.objects.all()

        return context


class ReviewsView(TemplateView):
    template_name = "toyfactory/reviews.html"

    def get_queryset(self):
        return Review.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.all()
        return context

    def post(self, request):
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            review = Review()
            review.clients_name = request.user
            review.rating = request.POST.get("rating")
            review.text = request.POST.get("text")
            review.save()
            return render(request, self.template_name, {"reviews": Review.objects.all()})
        return render(request, self.template_name, {"form": form, "reviews": Review.objects.all()})


class ProductView(ListView):
    model = Product
    template_name = "toyfactory/product_list.html"

    def get_queryset(self):
        if "product_type" not in self.kwargs:
            self.product_type = None
            return Product.objects.all()

        self.product_type = get_object_or_404(ProductType, id=self.kwargs["product_type"])
        return Product.objects.filter(type=self.product_type)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_type_list"] = ProductType.objects.all()

        if self.product_type is not None:
            context["product_type"] = self.product_type.id

        context["coupons"] = self.get_coupons()
        context["product_list"] = self.get_products()
        return context

    def get_products(self):
        refactor_dict = {}
        list_of_coupons = Product.objects.all().values_list("name", "price")
        for item in list_of_coupons:
            refactor_dict[item[0]] = item[1]
        return refactor_dict

    def get_coupons(self):
        refactor_dict = {}
        list_of_coupons = Coupon.objects.all().values_list("promo_code", "discount")
        for item in list_of_coupons:
            refactor_dict[item[0]] = item[1]
        return refactor_dict


class OrderFilter(django_filters.FilterSet):
    customer__name = django_filters.CharFilter(lookup_expr='icontains')
    product__name = django_filters.CharFilter(lookup_expr='icontains')
    quantity = django_filters.NumberFilter()
    quantity__gt = django_filters.NumberFilter(field_name='quantity', lookup_expr='gt')
    quantity__lt = django_filters.NumberFilter(field_name='quantity', lookup_expr='lt')
    date = django_filters.DateTimeFromToRangeFilter()
    completion_date = django_filters.DateTimeFromToRangeFilter()


class OrderView(LoginRequiredMixin, TemplateView):
    model = Order

    login_url = "accounts/login/"
    redirect_field_name = "redirect_to"
    template_name = "toyfactory/orders.html"


    def get(self, request, *args, **kwargs):
        base_queryset = Order.objects.all().order_by("-date") if request.user.is_superuser \
            else Order.objects.filter(manager=request.user.id).order_by("-date")

        filter = OrderFilter(request.GET, queryset=base_queryset)
        return render(request, self.template_name, {"object_list": filter.qs, "filter": filter})

    def post(self, request, *args, **kwargs):
        search_form = OrderSearchForm(request.POST)

        logging.debug("OrderView::post() called")

        if search_form.is_valid():
            current_customer = search_form.cleaned_data["customer"]
            current_product = search_form.cleaned_data["product"]


        return render(request, self.template_name, {"object_list": Order.objects.all(), "form": search_form})


class StatisticsView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "toyfactory/statistics.html"

    def get_queryset(self):
        refactor_dict = {}
        dict_of_quantities = Order.objects.all().values("product").annotate(Sum("quantity"))
        for item in dict_of_quantities:
            refactor_dict[Product.objects.get(id=item["product"]).name] = item["quantity__sum"]
        return refactor_dict

    def get_employees_profit(self):
        refactor_dict = {}
        list_of_quantities = Order.objects.all().values_list("manager", "product", "quantity")
        for item in list_of_quantities:
            refactor_dict[User.objects.get(id=item[0])] = Product.objects.get(id=item[1]).price * item[2]
        return refactor_dict

    def get_month_income(self):
        refactor_dict = {}
        list_of_dates = pd.period_range(start=Order.objects.all().order_by("date").values()[0]["date"],
                                        end=Order.objects.all().order_by("-date").values()[0]["date"], freq='M')
        for period in list_of_dates:
            date = period.to_timestamp().date()
            refactor_dict[date.strftime("%m/%d/%Y")] = 0

        for item in Order.objects.all():
            for period in list_of_dates:
                date = period.to_timestamp().date()
                if item.date.month == date.month and item.date.year == date.year:
                    refactor_dict[date.strftime("%m/%d/%Y")] += Product.objects.get(name=item.product).price * item.quantity
                    break
        return refactor_dict

    def get_customers(self):
        refactor_dict = {}
        dict_of_quantities = Order.objects.all().values("customer").annotate(Count("customer"))
        for item in dict_of_quantities:
            refactor_dict[Customer.objects.get(id=item["customer"]).name] = item["customer__count"]
        return refactor_dict

    def get_products_price(self):
        return Product.objects.all().values("code", "name", "price")

    def get_popular_product(self):
        product = Order.objects.all().values("product").annotate(Sum("quantity")).order_by("-quantity__sum")[0]
        product["product"] = Product.objects.get(id=product["product"]).name
        return product

    def get_less_popular_product(self):
        product = Order.objects.all().values("product").annotate(Sum("quantity")).order_by("quantity__sum")[0]
        product["product"] = Product.objects.get(id=product["product"]).name
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_list"] = Product.objects.all()
        context["employees_profit"] = self.get_employees_profit()
        context["month_income"] = self.get_month_income()
        context["customers"] = self.get_customers()
        context["products_price"] = self.get_products_price()
        context["popular_product"] = self.get_popular_product()
        context["less_popular_product"] = self.get_less_popular_product()
        return context
