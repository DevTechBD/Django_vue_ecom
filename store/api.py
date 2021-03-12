import stripe
from django.conf import settings

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product
import json

from cart.cart import Cart

from .models import Product

from order.utils import checkout
from order.models import Order, OrderItems



def stripe_checkout(request):
    cart = Cart(request)

    stripe.api_key = settings.STRIPE_API_HIDDEN_KEY
    
    items = []
    
    for item in cart:
        product = item['product']
        
        obj = {
            'price_data': {
                'currency': 'USD',
                'product_data': {
                    'name': product.title
                },
                'unit_amount': int(product.price * 100)  
            },
            'quantity': item['quantity']
        }
        
        items.append(obj)
        
        session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items = items,
            mode = 'payment',
            success_url = 'http://127.0.0.1:8000/checkout/success/',
            cancel_url = 'http://127.0.0.1:8000/cart/'
        )
        
        return JsonResponse({'session': session})
        




def api_checkout(request):
    data = json.loads(request.body)
    cart = Cart(request)
    
    jsonresponse = {'success': True}
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    zipcode = data['zipcode']
    place = data['place']
    
    
    orderId = checkout(request, first_name, last_name, email, address, zipcode, place)
    
    paid = True
    
    if paid == True:
        order = Order.objects.get(pk=orderId)
        order.paid = True
        order.paid_amount = cart.get_total_cost()
        
        order.save()
        cart.clear()
        
    return JsonResponse(jsonresponse)




def api_add_to_cart(request): 
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']
    update = data['update']
    
    quantity = data['quantity']
    
    cart = Cart(request)
    
    product = get_object_or_404(Product, pk=product_id)
    
    if not update:
        cart.add(product=product, quantity=1, updated_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, updated_quantity=True)
    
    
    return JsonResponse(jsonresponse)
    
    

def api_remove_from_cart(request):
    data = json.loads(request.body)
    
    jsonresp = {'success': True}
    
    product_id = str(data['product_id'])
    
    cart = Cart(request)
    
    cart.remove(product_id)
    
    return JsonResponse(jsonresp)