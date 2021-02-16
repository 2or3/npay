# coding: utf-8

from rest_framework import serializers

from .models import Transactions


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = (
            "user_id",
            "product_id",
            "charge",
            "created_at",
            "updated_at",
        )
