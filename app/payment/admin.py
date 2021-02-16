from django.contrib import admin

# Register your models here.
from .models import Transactions


@admin.register(Transactions)
class PaymentTransaction(admin.ModelAdmin):
    pass
