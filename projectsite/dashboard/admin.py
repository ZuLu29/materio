from django.contrib import admin

# Register your models here.
from .models import DevilFruitType, DevilFruit, Arc, ArcRating, ArcRanking

admin.site.register(DevilFruitType)
admin.site.register(DevilFruit)
admin.site.register(Arc)
admin.site.register(ArcRating)
admin.site.register(ArcRanking)