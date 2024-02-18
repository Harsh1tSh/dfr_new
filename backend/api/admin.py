from django.contrib import admin
from .models import Student
# Register your models here.
# connect the moels for the particular applications
# we can manage them from the admin interface

admin.site.register(Student)  