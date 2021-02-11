# coding: utf-8

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from coin import views
from coin.views import CoinViewSet


router = routers.DefaultRouter()
router.register(r'coins', CoinViewSet)

urlpatterns = [
    path('<int:user_id>/coin', views.coin_me),
]

urlpatterns = format_suffix_patterns(urlpatterns)
