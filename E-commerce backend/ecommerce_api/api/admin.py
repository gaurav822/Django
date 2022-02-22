from django.contrib import admin
from .models import Product, Users

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password','address']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','category']