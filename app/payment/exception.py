class CommonPaymentError(Exception):
    "Common Payment API Exception"


class CoinAPIRequestError(CommonPaymentError):
    "Coin API Request Error"
