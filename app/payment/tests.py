from django.test import TestCase

from .models import Payment

# Create your tests here.
class PaymentModelTests(TestCase):
    def test_charge_with_coin(self):
        """
        charge('coin') would returns coin balance if succeeded charge.
        """
        return

    def test_consume_with_coin(self):
        """
        consume('coin') would returns coin balance if succeeded consume.
        """
        return
