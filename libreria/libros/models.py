from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.CharField(max_length=200, default="link")
    birth_date = models.DateField()

    def get_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.first_name + " "+ self.last_name, self.id)

class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    year = models.IntegerField()
    cost = models.IntegerField()
    author =  models.ForeignKey(Author, on_delete=models.CASCADE)

    def get_book_name(self):
        return self.name

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.name, self.id)
