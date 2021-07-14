from django.db import models
from attrdict import AttrDict
from django.conf import settings
from .exception import CoinAPIRequestError

import requests


# Create your models here.
class TransactionManager(models.Manager):
    COIN_RESOURCE = "coins"
    USERS_COIN_RESOURCE = "coin"

    def charge(self, user_id, amount):
        get_url = f"{settings.BASE_URL}/{user_id}/{self.USERS_COIN_RESOURCE}"
        put_url = f"{settings.BASE_URL}{self.COIN_RESOURCE}"

        # Get Coin
        res = requests.get(get_url)
        if res.status_code != 200:
            raise CoinAPIRequestError

        if int(res.json["charge"]) < amount:
            return False

        # Update coin
        payload = {"user_id": user_id, "amount": amount}
        res = requests.put(put_url, data=payload)

        if res.status_code != 200:
            raise CoinAPIRequestError

        return True

    def get_charge(self, user_id, transaction_id):
        get_url = f"{settings.BASE_URL}/{user_id}/{self.USERS_COIN_RESOURCE}"

        # Get Coin
        res = requests.get(get_url)
        if res.status_code != 200:
            raise CoinAPIRequestError

        return AttrDict({"amount": int(res.json["charge"])})

    def list_charge(self, user_id):
        return [AttrDict({"amount": 3000})]


class Transactions(models.Model):
    objects = TransactionManager()

    user_id = models.IntegerField()
    product_id = models.IntegerField()
    charge = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
