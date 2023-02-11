from django.db.models import signals
from django.dispatch import receiver  
from django.db import models
import uuid

from core.models import BaseModel
from accounts.models import User
from items.models import Item


order_state_list = [
    ('pending', 'Pending'),
    ('cancelled', 'Cancelled'),
    ('confirm', 'Confirm'),
    ('on_the_way', 'On the way'),    
    ('delivered', 'Delivered'),    
]

payment_state_list = [
    ('pending', 'Pending'),
    ('cancelled', 'Cancelled'),
    ('confirm', 'Confirm') 
]


class Order(BaseModel):
    cutomer = models.ForeignKey(User, related_name='cutomer', on_delete=models.CASCADE)
    address = models.CharField(max_length= 500)
    mobile_no = models.CharField(max_length = 12)
    product = models.ForeignKey(Item, related_name='product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=1)
    total_cost = models.FloatField(default=1)
    order_status = models.CharField(max_length=50, choices=order_state_list, default="pending")
    payment_status = models.CharField(max_length=50, choices=payment_state_list, default="pending")
    transaction_id = models.UUIDField(default = uuid.uuid4, editable = False)

    def __str__(self):
        return str(self.transaction_id)


@receiver(signals.post_save, sender=Order) 
def create_order(sender, instance, created, **kwargs):
    if created:
        instance.product.quantity -= instance.quantity
        instance.product.save()
