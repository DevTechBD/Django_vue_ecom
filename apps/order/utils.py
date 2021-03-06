import os
import datetime


from random import randint

from apps.cart.cart import Cart
from apps.order.models import Order, OrderItems

def checkout(request, first_name, last_name, email, address, zipcode, place):
    order = Order(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place)
    
    order.save()
    
    cart = Cart(request)
    
    for item in cart:
        OrderItems.objects.create(order=order, product=item['product'], price = item['price'], quantity=item['quantity'])
    
    return order.id