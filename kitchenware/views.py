from django.shortcuts import render, redirect
from django.urls import reverse
from library.models.book import Book
from kitchenware.models.products import Product
from django.db.models import Q
# Create your views here.


def get_info(request):
    book = Book.objects.get(id=1)
    return render(request, 'base.html', context ={"book": book,})

# def get_author(request):
#     book_author = Book.objects.filter(author__name="Алекс Пушкин")
#     return render(request, 'author.html', context ={"book_author": book_author,})

def get_homepage(request): 
    return render(request, 'home.html')

def get_about(request): 
    return render(request, 'about.html')

def get_product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'detail_product.html', context ={"product": product,})
    

def get_products(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'products.html', context ={"products": products,})

def search_product(request):
    if request.method == "GET":
        search = request.GET['search']
        products = Product.objects.filter(
            Q(name__icontains = search) | Q(description__icontains = search))
        return render(request, template_name='products.html', context ={
            "products": products,
            "title": "Посуда"
    })
    return redirect(reverse('home'))