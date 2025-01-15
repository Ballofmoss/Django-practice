from django.db import models

class EntryPassword(models.Model): 
    website_name = models.CharField(max_length=100)
    website_url = models.CharField(max_length=255)

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    