from django.contrib import admin
from kitchenware.models import Product

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass
