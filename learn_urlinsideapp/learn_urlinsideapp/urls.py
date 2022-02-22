from django.contrib import admin
from django.urls import path, include

from course import views
from student import views as stuviews

# we can make list like below and pass to include at line 33
# studentpatt= [
# path('study/',stuviews.study,),
# path('study/',stuviews.study,)
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/',include('course.urls')),
    path('',include('fees.urls')),
    # path('',include('fees.urls')), => Directly checking to course.url  pattern
    path('',views.index),

    #Alternative way 1
    path('student/',include([
        path('study/',stuviews.study),
        path('play/',stuviews.play_basketball)
    ]))

    #Alternative way 2
    #line number 7

    
]
