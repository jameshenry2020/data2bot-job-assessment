from django.shortcuts import render
from .serializers import OrderItemSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Order


class CustomerOrders(ListAPIView):
    serializer_class=OrderItemSerializer
    permission_classes=[IsAuthenticated]


    def get_queryset(self):
        orders=Order.objects.filter(user=self.request.user, completed=True)
        if orders.exists():
            return orders
        return None

        