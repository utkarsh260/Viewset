from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    id = models.BigIntegerField(primary_key=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.CharField(('emailaddress'), unique = True, max_length = 200, null = True)
    mobile_no = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return self.name
