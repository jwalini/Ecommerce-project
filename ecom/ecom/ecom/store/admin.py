from django.contrib import admin
from .models import Product,Order,OrderItem

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'price']

class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'created_at']

class AdminOrderItem(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity', 'price_per_unit', 'subtotal']

admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
admin.site.register(OrderItem, AdminOrderItem)