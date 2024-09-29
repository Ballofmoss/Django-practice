from django.shortcuts import render, redirect
from .forms import OrderForm
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from cart.cart import CartSession
from .models import Order, OrderItem
from django.urls import reverse



@login_required(login_url='login')
def create_order(request: HttpRequest):
    cart = CartSession(request.session)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer_user = request.user
            order.save()
            for item_cart in cart:
                OrderItem.objects.create(order=order, product=item_cart['product'], quanity=item_cart['quanity']).save()
            cart.clear()
            return redirect(reverse('profile'))

    else:
        form = OrderForm()



