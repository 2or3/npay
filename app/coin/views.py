# coding: utf-8

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from coin.models import Coin
from coin.serializers import CoinSerializer


@api_view(['GET', 'PUT'])
def coin_me(request, user_id):
    """
    Get coin balance and modify coin.
    """
    if request.method == "GET":
        coin_amount = Coin.objects.get_amount(user_id=user_id)
        return Response(coin_amount)

    elif request.method == "PUT":
        coin = Coin.objects.get_amount(user_id=user_id)
        serializer = CoinSerializer(coin)
        return Response(serializer.data)

class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
