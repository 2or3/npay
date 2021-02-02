from django.db import models

# Create your models here.
class Coin(models.Model):
    user_id = models.IntegerField()
    amount = models.PositiveIntegerField()

class Transactions(models.Model):
    coin_id = models.ForeignKey(Coin, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    charge = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

