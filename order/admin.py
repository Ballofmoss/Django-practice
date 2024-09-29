from django.contrib import admin
from order.models.order import Order
from order.models.orderitem import OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_user', 'customer_email', 'order_date', 'status')
    search_fields = ('customer_user', 'customer_email', 'status')
    list_filter = ('status', 'order_date')
    inlines = [OrderItemInline]