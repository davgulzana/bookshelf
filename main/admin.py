from django.contrib import admin

from main.models import Book, Author, Genre, BookImage


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookImage)