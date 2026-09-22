from django.contrib import admin
from apps.address.models import UserAddress
# Register your models here.

@admin.register(UserAddress)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address_line']