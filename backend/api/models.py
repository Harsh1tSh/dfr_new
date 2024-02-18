from django.db import models

# Create your models here.
# models are basically our database tables and their fields
# beahaviour of the data it stores
# here we encapsulate the logic of quering manipulating and interacting
# with data by leveraging the django orm


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[("M","Male"),("F","Female"),("O","Other")])
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    major = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    is_active = models.BooleanField(default=True)
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
