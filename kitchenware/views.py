from django.shortcuts import render
from library.models.book import Book
from kitchenware.models.products import Product
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

def get_products(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'products.html', context ={"products": products,})


def get_publisher(request):
    book_publisher = Book.objects.filter(publishers__name="Rich")
    return render(request, 'publisher.html', context ={"book_publisher": book_publisher,})