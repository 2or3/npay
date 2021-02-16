# coding: utf-8

from rest_framework import status, viewsets
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from coin.models import Coin
from coin.serializers import CoinSerializer


@api_view(["GET", "PUT"])
@parser_classes([JSONParser])
def coin_me(request, user_id):
    """
    Get coin balance and modify coin.
    """
    if request.method == "GET":
        coin_amount = Coin.objects.get_amount(user_id=user_id)
        return Response(coin_amount)

    elif request.method == "PUT":
        coin = Coin.objects.calculate(
            user_id=user_id, value=request.data["value"]
        )
        return Response(coin)


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
