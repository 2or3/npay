from django.db import models

# Create your models here.
class Transactions(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    charge = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
