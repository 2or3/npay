from django.db import models, IntegrityError

# Create your models here.
class CoinManager(models.Manager):
    def calculate(self, user_id, value):
        try:
            result = Coin.objects.get_queryset().filter(user_id=user_id)
            pre_amount = result[0].amount

            Transactions.objects.create(coin_id=result[0], user_id=user_id, charge=value)

            post_amount = pre_amount + value
            Coin.objects.update_or_create(user_id=user_id, defaults={'amount': post_amount})

            result = Coin.objects.get_queryset().filter(user_id=user_id)
        except IntegrityError as e:
            return False

        if not result:
            return False

        return result[0].amount

    def get_amount(self, user_id):
        result = Coin.objects.get_queryset().filter(user_id=user_id)
        
        if not result:
            return False

        return result[0].amount

class Coin(models.Model):
    objects = CoinManager()

    user_id = models.IntegerField(unique=True)
    amount = models.PositiveIntegerField()

class Transactions(models.Model):
    coin_id = models.ForeignKey(Coin, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    charge = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

