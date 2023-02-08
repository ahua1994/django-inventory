from rest_framework import serializers
from .models import *


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = "__all__"


class PurchasesSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Purchases
        fields = "__all__"

    def get_total(self, obj):
        return obj.price * obj.quantity

    def validate(self, data):
        item = Product.objects.get(pk=data["product"].id) 
        if item.stock < data["quantity"]:
            raise serializers.ValidationError(
                f"There is not enough stock left ({item.stock}) to make this purchase.")
        else:
            item.stock = item.stock - data["quantity"]
            item.save()
        return super().validate(data)


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"
