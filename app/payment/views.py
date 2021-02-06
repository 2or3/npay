import django_filters
from rest_framework import viewsets, filters

from .models import Transactions
from .serializer import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = PaymentSerializer
