from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
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


class PurchasesUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     if serializer.validated_data.get("quantity") != instance.quantity:
    #         instance.quantity
    #     return super().update(request, *args, **kwargs)


class PurchasesListAllView(ListAPIView):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer


class SalesCreateView(CreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class SalesListAllView(CreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
