from django.contrib import admin
from .models import Student, User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','number','address')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','roll','city')