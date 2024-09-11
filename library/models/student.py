from django.db import models
from .course import Course

class Student(models.Model):
    name =  models.CharField(max_length=100)
    birth_date = models.DateField()
    courses = models.ManyToManyField(Course)