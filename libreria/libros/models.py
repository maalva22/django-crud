from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Author(models.Model):
    id= models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.CharField(max_length=200, default="link")
    birth_date = models.DateField()

    def get_name(self):
        return self.first_name + " " + self.last_name

class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    year = models.IntegerField()
    cost = models.IntegerField()
    author =  models.ForeignKey(Author, on_delete=models.CASCADE)


