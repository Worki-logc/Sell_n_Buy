from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=122)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pic = models.ImageField(upload_to="./Images")
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def _str_(self):
        return f"Cart {self.id} for {self.user.username}"

class cart_item(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"