from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('tshirt', 'T-Shirts'),
        ('shirt', 'Shirts'),
        ('jeans', 'Jeans'),
        ('trouser', 'Trousers'),
        ('jacket', 'Jackets'),
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name   

class Order(models.Model):
    STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
]
    

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    