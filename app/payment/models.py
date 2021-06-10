from django.db import models
from attrdict import AttrDict
from django.conf import settings

import requests


# Create your models here.
class TransactionManager(models.Manager):
    def charge(self, user_id, amount):
        url = f"{settings.COIN_BASE_URL}"
        payload = {"user_id": user_id, "amount": amount}
        requests.put(url, data=payload)
        if amount > 1000:
            return False

        return True

    def get_charge(self, user_id, transaction_id):
        return AttrDict({"amount": 1000})

    def list_charge(self, user_id):
        return [AttrDict({"amount": 1000})]


class Transactions(models.Model):
    objects = TransactionManager()

    user_id = models.IntegerField()
    product_id = models.IntegerField()
    charge = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
