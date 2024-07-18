from django.contrib import admin
from .models import Customer, ProductType, ProductModel, Product, Order, Review, Article, Coupon


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "city", "address", "phone")
    fieldsets = [
        (None, {"fields": ["code", "name"]}),
        ("Contacts", {"fields": ["city", "address", "phone"]}),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "product", "completion_date", "quantity", "date", "manager")
    list_filter = ("customer", "product")
    fieldsets = [
        (None, {"fields": ["customer", "manager", "product", "quantity"]}),
        ("Dates", {"fields": ["date", "completion_date"]}),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "code", "type", "model", "price", "image", "in_production")
    list_filter = ("type", "model", "in_production")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("clients_name", "rating", "text", "date")
    list_filter = ("clients_name", "rating", "date")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "summary", "text", "image", "date")
    list_filter = ("title", "text", "date")


class CouponAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date", "description", "image", "promo_code", "discount")
    list_filter = ("title", "date")


admin.site.register(Customer, CustomerAdmin)
admin.site.register(ProductType)
admin.site.register(ProductModel)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Coupon, CouponAdmin)
