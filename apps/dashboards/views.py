from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import ExtractYear

from .models import Movie, Genre, Character

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""


class DashboardsView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

def movies_over_time(request):
    data = (
        Movie.objects
        .annotate(year=ExtractYear('release_date'))
        .values('year')
        .annotate(count=Count('id'))
        .order_by('year')
    )
    return JsonResponse({
        'years': [entry['year'] for entry in data],
        'counts': [entry['count'] for entry in data]
    })

def genre_distribution(request):
    data = (
        Movie.objects
        .values('genre__name')
        .annotate(count=Count('id'))
        .order_by('genre__name')
    )
    return JsonResponse({
        'labels': [entry['genre__name'] for entry in data],
        'counts': [entry['count'] for entry in data]
    })

def character_movie_counts(request):
    data = (
        Character.objects
        .annotate(movie_count=Count('movies'))
        .filter(movie_count__gt=0)
        .values('name', 'movie_count')
        .order_by('-movie_count')
    )
    return JsonResponse({
        'characters': [entry['name'] for entry in data],
        'counts': [entry['movie_count'] for entry in data]
    })
def most_featured_strawhats(request):
    strawhats = ['Monkey D. Luffy', 'Roronoa Zoro', 'Nami', 'Sanji', 'Usopp', 'Chopper', 'Robin', 'Franky', 'Brook', 'Jinbe']

    data = (
        Character.objects
        .filter(name__in=strawhats)
        .annotate(movie_count=Count('movies'))
        .values('name', 'movie_count')
        .order_by('-movie_count')
    )
    return JsonResponse({
        'labels': [entry['name'] for entry in data],
        'counts': [entry['movie_count'] for entry in data]
    })
