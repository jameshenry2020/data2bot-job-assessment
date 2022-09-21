from functools import partial
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from customers.models import Profile
from .serializers import UserSerializer, LoginUserSerializer, UpdateProfileSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterCustomer(GenericAPIView):
    serializer_class=UserSerializer
    def post(self, request, *args, **kwargs):
        incoming_data=request.data
        serializer=self.serializer_class(data=incoming_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            return Response(user, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginCustomer(GenericAPIView):
    serializer_class=LoginUserSerializer
    def post(self, request):
        serializer=self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserProfileInfo(GenericAPIView):
    serializer_class= UpdateProfileSerializer
    permission_classes=[IsAuthenticated]

    def patch(self, request):
        try:
            profile= Profile.objects.get(user=request.user)

        except Profile.DoesNotExist:
            raise NotFound
        
        data=request.data
        serializer=self.serializer_class(instance=profile, data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    


