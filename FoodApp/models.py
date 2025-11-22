from django.db import models

class ProductCategory(models.TextChoices):
    BURGER = 'burger', 'Burger'
    PIZZA = 'pizza', 'Pizza'
    DRINK = 'drink', 'Drink'
    DESSERT = 'dessert', 'Dessert'
    SANDWICH = 'sandwich', 'Sandwich'
    OTHER = 'other', 'Other'


class OrderStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    PREPARING = 'preparing', 'Preparing'
    ON_THE_WAY = 'on_the_way', 'On the Way'
    DELIVERED = 'delivered', 'Delivered'
    CANCELED = 'canceled', 'Canceled'

class TrackingStatus(models.TextChoices):
    ASSIGNED = 'assigned', 'Assigned'
    PICKING_UP = 'picking_up', 'Picking Up'
    ON_THE_WAY = 'on_the_way', 'On the Way'
    DELIVERED = 'delivered', 'Delivered'

class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'customers'


class Restaurant(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)

    phone = models.CharField(max_length=20, null=True, blank=True)
    image_url = models.CharField(max_length=500, null=True, blank=True)

    delivery_time = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'restaurants'


class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(
        'Restaurant',
        on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    image_url = models.CharField(max_length=500, null=True, blank=True)

    category = models.CharField(
        max_length=100,
        choices=ProductCategory.choices,
        default=ProductCategory.OTHER
    )

    class Meta:
        db_table = 'products'


class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        related_name='orders'
    )

    restaurant = models.ForeignKey(
        'Restaurant',
        on_delete=models.CASCADE,
        related_name='orders'
    )

    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'


class OrderItem(models.Model):
    OrderItemID = models.AutoField(primary_key=True)
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='order_items'
    )

    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'order_items'
        unique_together = ('order', 'product')



class OrderTracking(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name='tracking'
    )

    status = models.CharField(
        max_length=50,
        choices=TrackingStatus.choices,
        default=TrackingStatus.ASSIGNED
    )

    current_latitude = models.DecimalField(
        max_digits=10,
        decimal_places=8,
        null=True,
        blank=True
    )

    current_longitude = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        null=True,
        blank=True
    )

    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_tracking'

