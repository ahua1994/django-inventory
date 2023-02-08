from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView
from django.contrib.auth.models import User
from .serializers import *


class FirmCreateView(CreateAPIView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class FirmListAllView(ListAPIView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class PurchasesCreateView(CreateAPIView):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer


class PurchasesListAllView(CreateAPIView):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer


class SalesCreateView(CreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class SalesListAllView(CreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
