from django.urls import path
from .views import RegisterCustomer, LoginCustomer, UpdateUserProfileInfo


urlpatterns=[
    path('register/', RegisterCustomer.as_view(), name='register'),
    path('login/', LoginCustomer.as_view(), name='customer-login'),
    path('edit-profile/', UpdateUserProfileInfo.as_view(), name='profile-update')
]