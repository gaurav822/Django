
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productinfo/<int:pk>',views.product_detail),
    path('userinfo/<int:pk>',views.user_detail),
    path('users/',views.user_list),
    path('products/',views.product_list),
    path('signup/',views.user_create)

]
