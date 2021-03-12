from django.shortcuts import render, redirect
from .models import *

# Create your views here.



def home(request):
    products = Product.objects.all()
    logos = Logo.objects.all()
    sliders = Slider.objects.all()[:1]
    cats = Category.objects.all()
    
    args = {'products': products, 'logos': logos, 'sliders': sliders, 'cats': cats}
    return render(request, 'home.html', args)

def product_details(request, id):
    products = Product.objects.get(pk=id)
    logos = Logo.objects.all()
    
        
    
    args = {'products': products, 'logos': logos}
    
    return render(request, 'p_details.html', args)


def success(request):
    return render(request, 'success.html')
