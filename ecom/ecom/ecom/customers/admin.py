from django.contrib import admin
from .models import User, Address

class AdminAddress(admin.ModelAdmin):
    list_display = ['id', 'street', 'city', 'state', 'country', 'pincode', 'landmark']


class AdminUser(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone_number', 'address']


admin.site.register(Address, AdminAddress)
admin.site.register(User, AdminUser)