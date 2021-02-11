# coding: utf-8

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from coin import views


urlpatterns = [
    path('<int:user_id>/coins', views.coin_me),
]

urlpatterns = format_suffix_patterns(urlpatterns)
