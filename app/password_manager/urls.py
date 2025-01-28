
from .views.base import HomeView, WebSiteDataDetailView, WebsiteDataCreateView, WebsiteDataUpdateView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<int:pk>', WebSiteDataDetailView.as_view(), name="website_data_detail"),
    path('create', WebsiteDataCreateView.as_view(), name="website_data_create"),
    path('update/<int:pk>', WebsiteDataUpdateView.as_view(), name="website_data_update"),
]