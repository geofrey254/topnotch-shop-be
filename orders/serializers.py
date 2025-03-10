from rest_framework import serializers
from .models import Order, OrderItem
from payments.serializers import ShippingSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    shipping_address = ShippingSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
