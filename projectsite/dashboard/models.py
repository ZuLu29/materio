from django.db import models

# Create your models here.
from django.db import models

# Base model for timestamps
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Types of Devil Fruits: Paramecia, Zoan, Logia, etc.
class DevilFruitType(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Individual Devil Fruits
class DevilFruit(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    type = models.ForeignKey(DevilFruitType, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    current_user = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name


# Arcs within the One Piece series
class Arc(BaseModel):
    name = models.CharField(max_length=150)
    saga = models.CharField(max_length=150, blank=True)  # e.g., East Blue Saga, Alabasta Saga
    start_episode = models.PositiveIntegerField()
    end_episode = models.PositiveIntegerField()
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.name


# User or critic ratings for arcs
class ArcRating(BaseModel):
    arc = models.ForeignKey(Arc, on_delete=models.CASCADE, related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # e.g., 9.5
    reviewer = models.CharField(max_length=100)  # could be user or critic name

    def __str__(self):
        return f"{self.arc.name} - {self.rating}"


# Rankings, e.g., by fan polls or reviews
class ArcRanking(BaseModel):
    arc = models.OneToOneField(Arc, on_delete=models.CASCADE)
    rank_position = models.PositiveIntegerField()
    ranked_by = models.CharField(max_length=150)  # e.g., "Fan Poll 2024"

    def __str__(self):
        return f"{self.arc.name} - Rank #{self.rank_position}"
