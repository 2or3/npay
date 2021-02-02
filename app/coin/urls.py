# coding: utf-8

from rest_framework import routers
from .views import CoinViewSet


router = routers.DefaultRouter()
router.register(r'coins', CoinViewSet)

