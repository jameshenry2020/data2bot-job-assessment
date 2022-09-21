
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import Profile, User
from django.contrib.auth import authenticate




class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=64, min_length=6, write_only=True)
    retype_password=serializers.CharField(max_length=64, min_length=6, write_only=True)

    class Meta:
        model=User
        fields=['email', 'first_name','last_name', 'password', 'retype_password']


    def validate(self, attrs):
        email=attrs.get('email')
        password=attrs.get('password')
        retype_password=attrs.get('retype_password')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('user with that email already exist') 
        if password != retype_password:
            raise serializers.ValidationError('passwords do not match')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            password=validated_data.get('password')
        )

class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=10)
    password=serializers.CharField(max_length=60, min_length=6, write_only=True)
    first_name=serializers.CharField(max_length=200, read_only=True)
    last_name=serializers.CharField(max_length=200, read_only=True)
    tokens=serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields=['email', 'password', 'first_name', 'last_name', 'tokens']

    def validate(self, attrs):
        print(attrs)
        email = attrs.get('email')
        raw_password=attrs.get('password')
        request=self.context.get('request')
        user = authenticate(request, email=email, password=raw_password)
        print(user)
        if not user:
            raise AuthenticationFailed('invalid credentials try again')

        return {
            'email':user.email,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'tokens':user.tokens
        }



class UpdateProfileSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(source="user.first_name")
    last_name=serializers.CharField(source="user.last_name")
    class Meta:
        model=Profile
        fields = ['first_name', 'last_name', 'phone_number', 'country', 'city', 'gender']


    def update(self, instance, validated_data):
        user=instance.user
        user.first_name=validated_data['user'].get('first_name', instance.user.first_name)
        user.last_name=validated_data['user'].get('last_name', instance.user.last_name)
        instance.phone_number=validated_data.get('phone_number', instance.phone_number)
        instance.country=validated_data.get('country', instance.country)
        instance.city=validated_data.get('city', instance.city)
        instance.gender=validated_data.get('gender', instance.gender)
        instance.save()
        user.save()
        return instance
        
        


        