# coding: utf-8

from rest_framework import routers
from .views import PaymentViewSet


router = routers.DefaultRouter()
router.register(r'payments', PaymentViewSet)
