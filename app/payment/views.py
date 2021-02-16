from rest_framework import viewsets

from .models import Transactions
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = PaymentSerializer
