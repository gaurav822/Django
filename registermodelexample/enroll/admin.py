from django.contrib import admin
from enroll.models import Student
from modeladminexample.models import Person
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=('id','pid','pname','pemail','ppass')
 
#This is return object in admin site
#admin.site.register(Student)

#Now this will show details since we have used ModelAdmin method
admin.site.register(Person,PersonAdmin)

#The best way in below by using the decorator

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('stuid','stuname','stuemail','stupass')



