from django.urls import path
from .views import get_homepage, get_about, get_products

urlpatterns = [
    path('home/', get_homepage, name='home'),
    path('about/', get_about, name='about'),
    path('products/', get_products, name='products'),
]