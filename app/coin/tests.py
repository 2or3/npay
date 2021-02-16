from django.test import TestCase

from .models import Coin

# Create your tests here.
class CoinModelTests(TestCase):
    fixtures = ["fixture1"]

    def setUp(self):
        self.user_id = "1234567890"
        self.not_exist_user_id = "1111111111"
        return

    def test_calculate_with_positive_amount(self):
        """
        calculate() with positive amount returns coin amount if succeeded coin calculation.
        """
        before_amount = Coin.objects.get_amount(self.user_id)
        add_coin_value = 100
        after_amount = Coin.objects.calculate(self.user_id, add_coin_value)
        self.assertEqual(after_amount, before_amount + add_coin_value)

    def test_calculate_with_minus_amount(self):
        """
        calculate() with minus amount returns coin amount if succeeded coin calculation.
        """
        before_amount = Coin.objects.get_amount(self.user_id)
        add_coin_value = -100
        after_amount = Coin.objects.calculate(self.user_id, add_coin_value)
        self.assertEqual(after_amount, before_amount + add_coin_value)

    def test_calculate_with_exceeded_minus_amount(self):
        """
        calculate() with exceeded minus amount returns False if negative value exceeded coin amount.
        """
        add_coin_value = -1000
        after_amount = Coin.objects.calculate(self.user_id, add_coin_value)
        self.assertFalse(after_amount)

    def test_calculate_with_not_exist_user_id(self):
        """
        calculate() returns False if  no exist user_id.
        """
        add_coin_value = 100
        after_amount = Coin.objects.calculate(
            self.not_exist_user_id, add_coin_value
        )
        self.assertFalse(after_amount)

    def test_get_amount_with_user_id(self):
        """
        get_amount() for specific user returns valid amount if succeeded coin amount get. Please see fixture1 for default data.
        """
        expected_amount = 100
        amount = Coin.objects.get_amount(self.user_id)
        self.assertEqual(expected_amount, amount)

    def test_get_amount_with_not_exist_user_id(self):
        """
        get_amount() returns false if no exist user_id.
        """
        amount = Coin.objects.get_amount(self.not_exist_user_id)
        self.assertEqual(False, amount)
