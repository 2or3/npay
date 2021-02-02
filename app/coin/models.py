from django.db import models

# Create your models here.
class CoinManager(models.Manager):
    def calculate(self, user_id, value):
        return 10

    def get_amount(self, user_id):
        result = super().get_queryset().filter(user_id=user_id)
        return result[0].amount

class Coin(models.Model):
    objects = CoinManager()

    user_id = models.IntegerField()
    amount = models.PositiveIntegerField()

class Transactions(models.Model):
    coin_id = models.ForeignKey(Coin, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    charge = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

