from django.urls import path
from .views import get_author, get_publisher

urlpatterns = [
    path('author/', get_author),
    path('publisher/', get_publisher),
]