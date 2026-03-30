from django.contrib import admin
from .models import Author, Publisher, Book, Human

# Basic registration
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Human)
