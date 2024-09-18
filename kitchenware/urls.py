from django.urls import path
from .views import get_homepage, get_about, get_products, get_product_detail, search_product

urlpatterns = [
    path('home/', get_homepage, name='home'),
    path('about/', get_about, name='about'),
    path('products/', get_products, name='products'),
    path('product/<int:pk>', get_product_detail, name='product_detail'),
    path('product/search', search_product, name="search")             
]