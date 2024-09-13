from rest_framework import serializers
from .models import Product,UserProfile
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('id','name','description','price')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields=('username', 'first_name', 'last_name', 'email', 'cv', 'photo', 'id_photo')

# class UserSerializer