from django.db import models
 
class Course(models.Model):
    title =  models.CharField(max_length=100)
    start_date = models.DateField()
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)