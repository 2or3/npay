from django.test import TestCase

from .models import Transactions
from .exception import CoinAPIRequestError
from unittest import mock


# Define mock response class.
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


# Create your tests here.
class PaymentModelTests(TestCase):
    fixtures = ["fixture1"]

    mock_res = MockResponse("", 200)
    mock_ng_res = MockResponse("", 400)
    mock_get_res = MockResponse("3000", 200)
    mock_get_ng_res = MockResponse("", 400)
    mock_list_res = MockResponse([{"charge": 3000}], 200)

    def setUp(self):
        self.user_id = "1234567890"
        return

    @mock.patch("payment.models.requests.put", mock.MagicMock(return_value=mock_res))
    @mock.patch("payment.models.requests.get", mock.MagicMock(return_value=mock_get_res))
    def test_create_payment(self):
        """
        post payment('user', 'amount') would returns true if succeeded charge.
        """
        add_coin_value = 100
        result = Transactions.objects.charge(self.user_id, add_coin_value)
        self.assertTrue(result)

    @mock.patch("payment.models.requests.get", mock.MagicMock(return_value=mock_get_res))
    def test_create_payment_with_over_amount(self):
        """
        post payment('user', 'amount') would returns false with over charge.
        """

        add_coin_value = 10000
        result = Transactions.objects.charge(self.user_id, add_coin_value)
        self.assertFalse(result)

    @mock.patch("payment.models.requests.put", mock.MagicMock(return_value=mock_ng_res))
    @mock.patch("payment.models.requests.get", mock.MagicMock(return_value=mock_get_ng_res))
    def test_create_payment_with_file_get_coin(self):
        """
        post payment('user', 'amount') would returns false if coin get returned ng.
        """
        add_coin_value = 100
        with self.assertRaises(CoinAPIRequestError):
            Transactions.objects.charge(self.user_id, add_coin_value)

    @mock.patch("payment.models.requests.put", mock.MagicMock(return_value=mock_ng_res))
    @mock.patch("payment.models.requests.get", mock.MagicMock(return_value=mock_get_res))
    def test_create_payment_with_file_put_coin(self):
        """
        post payment('user', 'amount') would returns false if coin put returned ng.
        """
        add_coin_value = 100
        with self.assertRaises(CoinAPIRequestError):
            Transactions.objects.charge(self.user_id, add_coin_value)

    @mock.patch("payment.models.requests.get", mock.MagicMock(return_value=mock_get_res))
    def test_show_payment(self):
        """
        get payment('user', 'transaction') would returns payment by transaction.
        """
        transaction_id = 1
        result = Transactions.objects.get_charge(self.user_id, transaction_id)
        self.assertEqual(result.amount, 3000)

    @mock.patch("payment.models.requests.get", mock.MagicMock(return_value=mock_list_res))
    def test_list_payment(self):
        """
        list_payment('user') would returns all payment list for user.
        """
        result = Transactions.objects.list_charge(self.user_id)
        self.assertCountEqual(result, [{"amount": 3000}])
        self.assertEqual(result, [{"amount": 3000}])
