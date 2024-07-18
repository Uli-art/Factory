from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'product_types', api.ProductTypeViewSet)
router.register(r'orders', api.OrderViewSet)
router.register(r'product_models', api.ProductModelViewSet)
router.register(r'products', api.ProductViewSet)
router.register(r'customers', api.CustomerViewSet)
router.register(r'users', api.UserViewSet)
router.register(r'review', api.ReviewTypeViewSet)
router.register(r'article', api.ArticleTypeViewSet)
router.register(r'coupon', api.CouponTypeViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("products", views.ProductView.as_view(), name="products"),
    path("orders", views.OrderView.as_view(), name="orders"),
    path("stat", views.StatisticsView.as_view(), name="stat"),
    path("products/<int:product_type>/", views.ProductView.as_view(), name="product_by_type"),
    path("about_us", views.AboutUsView.as_view(), name="about_us"),
    path("questions", views.QuestionsView.as_view(), name="questions"),
    path("privacy_policy", views.PrivacyPolicyView.as_view(), name="privacy_policy"),
    path("contacts", views.ContactsView.as_view(), name="contacts"),
    path("vacancies", views.VacanciesView.as_view(), name="vacancies"),
    path("coupons", views.CouponsView.as_view(), name="coupons"),
    path("news", views.NewsView.as_view(), name="news"),
    path("news/<int:news_id>/", views.ArticleView.as_view(), name="article"),
    path("reviews", views.ReviewsView.as_view(), name="reviews"),
    path("additional", views.AdditionalView.as_view(), name="additional")
]

urlpatterns += staticfiles_urlpatterns()