# coding: utf-8

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from payment import views
from payment.views import PaymentViewSet


router = routers.DefaultRouter()
router.register(r"payments", PaymentViewSet)

urlpatterns = [
    path("<int:user_id>/payments", views.users_payments),
]

urlpatterns = format_suffix_patterns(urlpatterns)
