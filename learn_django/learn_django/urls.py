"""learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from course import views as cv
from fees import views as fv
from django.contrib import admin
from django.urls import path

#alternative way
from course.views import learn_django
# path('learndj',learn_django)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/',cv.learn_django),
    path('altlearndj/',cv.learn_django), # we can can define multiple url for same function
    path('learnpy/',cv.learn_python),
    path('learnmath/',cv.learn_math),
    path('learnfor/',cv.learn_format),
    path('',cv.index),
    path('payfees/',fv.pay_fees)
    #  path('',views.learn_django), we can do this as well

]       
