from rest_framework import serializers
from .models import Order, OrderedProduct
from django.contrib.auth import get_user_model
User = get_user_model()
#


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class OrderedProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderedProduct
        fields = '__all__'
        depth = 1


class OrderedProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderedProduct
        fields = '__all__'


class CheckoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        depth = 2


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
