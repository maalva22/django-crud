from django.contrib import admin

# Register your models here.
from .models import Author

admin.site.register(Author)

from .models import Book

admin.site.register(Book)