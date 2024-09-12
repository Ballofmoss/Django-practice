from django.urls import path
from .views import get_author, get_publisher

urlpatterns = [
    path('home/', get_author),
    path('publisher/', get_publisher),
]