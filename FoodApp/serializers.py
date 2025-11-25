from rest_framework import serializers
from .models import Customer, Restaurant, Product, Order, OrderItem, OrderTracking

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTracking
        fields = "__all__"



class CustomerBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ( "full_name", "phone")




class AddCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'email', 'password', 'full_name', 'phone']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_email(self, value):
        # Instance = l'utilisateur actuel lors d'un update
        customer_id = self.instance.id if self.instance else None
        
        # Vérifie si un autre utilisateur (≠ moi) utilise cet email
        if Customer.objects.exclude(id=customer_id).filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")

        return value
