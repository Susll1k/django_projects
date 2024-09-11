from rest_framework import serializers
from .models import Product,UserProfile

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('id','name','description','price')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields=('username', 'first_name', 'last_name', 'email', 'cv', 'photo', 'id_photo')