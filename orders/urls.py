from django.urls import path
from .views import CustomerOrders



urlpatterns = [
    path('orders/', CustomerOrders.as_view(), name='orders'),
    ]