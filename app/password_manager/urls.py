
from .views.base import HomeView, WebSiteDataDetailView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<int:pk>', WebSiteDataDetailView.as_view(), name="website_data_detail")
]