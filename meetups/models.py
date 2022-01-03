from django.db import models

# Create your models here.
# creates a blueprint for our objects and for our database

class Meetup(models.Model):
    title = models.CharField(max_length=200) # text is expected in a database table 
    slug = models.SlugField(unique=True) # verifies that duplicate slugs DNE
    email = models.EmailField(max_length=200)
    description = models.TextField()