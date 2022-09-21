from rest_framework import serializers
from .models import Order, Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id', 'name', 'description', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    products=serializers.SerializerMethodField(read_only=True)
    total_price=serializers.SerializerMethodField()

    class Meta:
        model=Order
        fields=[
            'id',
            'products',
            'quantity',
            'payment_method',
            'total_price',
            'timestamp',
            'completed'
        ]

    def get_products(self, obj):
        return ProductSerializer(obj.product).data

    def get_total_price(self , obj):
        return obj.get_total_item_price()

    





