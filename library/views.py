from django.shortcuts import render

# Create your views here.
def get_book(request):
    return render(request, 'book.html', {'title': 'война и Мир', 'content': 'Страница книги "война и Мир"'})