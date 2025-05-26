
# Register your models here.
from django.contrib import admin

from .models import Genre, Director, Character, Movie

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Character)
admin.site.register(Movie)
