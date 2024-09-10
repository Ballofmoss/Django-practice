from django.db import models

class book(models.Model):
    name =  models.CharField(max_length=255)
    author = models.CharField(max_length=10)
    year = models.CharField(max_length=4, null=True)
    
class Author(models.Model):
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=35)
    

