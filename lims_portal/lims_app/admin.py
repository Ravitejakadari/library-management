from django.contrib import admin
from .models import *
from .models import Book
# Register your models here.
admin.site.register(reader)
admin.site.register(Book)