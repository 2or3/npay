class CommonCoinError(Exception):
    "Common Coin API Exception"


class CoinNoDataError(CommonCoinError):
    "Coin API No Data Exception"


class CoinEntityIntegrityError(CoinNoDataError):
    "Coin Entity Integrity Error"


class CoinNoDataByUserError(CoinEntityIntegrityError):
    "Coin API No Data By User Exception"
