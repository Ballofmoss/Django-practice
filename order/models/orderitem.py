from django.db import models
from .order import Order
from kitchenware.models import Product
 
    

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quanity = models.IntegerField()
    
    def __str__(self):
        return f"{self.quanity} of {self.product} for {self.order}"
    