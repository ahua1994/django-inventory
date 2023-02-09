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
        # if self.context.get("request").method == "PUT":
        #     print(self)
        item = Product.objects.get(pk=data["product"].id)
        if str(data["brand"]) not in str(data["product"]):
            raise serializers.ValidationError(
                f"{data['brand']} does not have this product")
        if data["price"] <= 0:
            raise serializers.ValidationError(
                f"This item cannot cost {data['price']}!")
        if item.stock < data["quantity"]:
            raise serializers.ValidationError(
                f"There is not enough stock left ({item.stock}) to make this purchase.")
        elif item.stock == 0:
            raise serializers.ValidationError(
                f"{item.name} is sold out.")
        elif data["quantity"] <= 0:
            raise serializers.ValidationError(
                f"You must purchase atleast one product.")
        else:
            item.stock = item.stock - data["quantity"]
            item.save()
        return super().validate(data)


class SalesSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Sales
        fields = "__all__"

    def get_total(self, obj):
        return obj.price * obj.quantity

    def validate(self, data):
        if str(data["brand"]) not in str(data["product"]):
            raise serializers.ValidationError(
                f"{data['brand']} does not have this product")
        if data["price"] <= 0:
            raise serializers.ValidationError(
                f"This item cannot cost {data['price']}!")
        elif data["quantity"] <= 0:
            raise serializers.ValidationError(
                f"You must sell atleast one product.")
