from rest_framework import viewsets
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from payment.models import Transactions
from payment.serializers import PaymentSerializer


@api_view(["GET", "PUT"])
@parser_classes([JSONParser])
def users_payments(request, user_id):
    """
    Get payments and charge.
    """
    return Response(Transactions.objects.all())


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = PaymentSerializer
