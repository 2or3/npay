# coding: utf-8

from rest_framework import serializers

from .models import Coin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin 
        fields = ('user_id', 'amount')

