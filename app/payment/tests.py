from django.test import TestCase

from .models import Transactions

# Create your tests here.
class PaymentModelTests(TestCase):
    fixtures = ["fixture1"]

    def setUp(self):
        self.user_id = "1234567890"
        return

    def test_create_payment(self):
        """
        post payment('user', 'amount') would returns true if succeeded charge.
        """
        add_coin_value = 100
        result = Transactions.objects.charge(self.user_id, add_coin_value)
        self.assertTrue(result)

    def test_create_payment_with_over_amount(self):
        """
        post payment('user', 'amount') would returns false with over charge.
        """
        add_coin_value = 10000
        result = Transactions.objects.charge(self.user_id, add_coin_value)
        self.assertFalse(result)

    def test_update_payment(self):
        """
        put payment('transaction', 'amount') would returns payment by transaction.
        """
        return

    def test_show_payment(self):
        """
        get payment('transaction') would returns payment by transaction.
        """
        return

    def test_list_payment(self):
        """
        list_payment('user') would returns all payment list for user.
        """
        return
