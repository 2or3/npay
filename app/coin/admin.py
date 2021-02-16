from django.contrib import admin

# Register your models here.
from .models import Coin, Transactions


@admin.register(Coin)
class Coin(admin.ModelAdmin):
    pass


@admin.register(Transactions)
class CoinTransaction(admin.ModelAdmin):
    pass
