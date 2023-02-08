from rest_framework import serializers
from .models import *


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = "__all__"


class PurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = "__all__"


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"
