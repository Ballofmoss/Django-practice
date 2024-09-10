from django.db import models
 
class Book(models.Model):
    title =  models.CharField(max_length=100)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Publisher)