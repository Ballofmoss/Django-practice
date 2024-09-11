from django.db import models
from .teacher import Teacher
 
class Course(models.Model):
    title =  models.CharField(max_length=100)
    start_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)