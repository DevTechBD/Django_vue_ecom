"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from cart.views import *

from store.api import api_add_to_cart, api_remove_from_cart, api_checkout, stripe_checkout
from ecommerce import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    
    ## Products Details URL
    
    path('<int:id>', views.product_details, name="product_details"),
    
    ## Cart View ##
    
    path('cart/', cart_details, name="cart_details"),
    
    ## API
    
    path('api/api_add_to_cart/', api_add_to_cart, name="api_add_to_cart"),
    path('api/api_remove_from_cart/', api_remove_from_cart, name="api_remove_from_cart"),
    
    ## Order APi ##
    
    path('api/api_checkout/', api_checkout, name="api_checkout"),
    
    ## Stripe Success Page ##
    
    path('checkout/success/', views.success, name="success"),
    
    ## Stripe Checkout URL
    
    path('api/stripe_checkout/', stripe_checkout, name="stripe_checkout"),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)