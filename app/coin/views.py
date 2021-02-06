# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import Coin
from .serializer import CoinSerializer


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
