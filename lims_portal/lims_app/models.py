from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id=models.CharField(max_length=200)
    reader_name=models.CharField(max_length=200)
    reader_cantact=models.CharField(max_length=200)
    reader_address=models.TextField()
    active=models.BooleanField(default=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    quantity_available = models.IntegerField(default=0)

    def __str__(self):
        return self.title 

