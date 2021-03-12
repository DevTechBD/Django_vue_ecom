from django.shortcuts import render

from django.conf import settings

from cart.cart import Cart
from order.models import *
from store.models import Logo

# Create your views here.


def cart_details(request):
    cart = Cart(request)
    logos = Logo.objects.all()
    productString = ""
    
    for item in cart:
        product = item['product']
        b = "{'id':'%s','title':'%s','price':'%s','quantity':'%s', 'total_price':'%s'},"%(product.id, product.title, product.price, item['quantity'], item['total_price'])
        
        productString = productString + b
        
    context = {
        'cart': cart,
        'pub_key': settings.STRIPE_API_PUBLISHABLE_KEY,
        'productString': productString,
        'logos': logos
    
        
    }
    
    return render(request, 'cart.html', context)