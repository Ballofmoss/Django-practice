from django.shortcuts import render

# Create your views here.

def get_base(request):
    return render(request, 'home.html', {
        'title': 'base',
    })
    
def o_nas(request):
    return render(request, 'onas.html', {
        'title': 'onas',
    })