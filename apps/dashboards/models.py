from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    actor = models.CharField(max_length=100, blank=True)
    role_description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    summary = models.TextField()
    duration_minutes = models.PositiveIntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    characters = models.ManyToManyField(Character, related_name='movies')

    def __str__(self):
        return self.title
