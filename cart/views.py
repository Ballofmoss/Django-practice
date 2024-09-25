from django.shortcuts import render, redirect, get_object_or_404
from .cart import CartSession
from django.http import HttpRequest
from kitchenware.models import Product
from django.urls import reverse

def cart_add(request: HttpRequest, product_id):
    cart = CartSession(request.session)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    
    return redirect(reverse('cart_detail'))

def cart_remove(request: HttpRequest, product_id):
    cart = CartSession(request.session)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
