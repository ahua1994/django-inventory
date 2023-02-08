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
