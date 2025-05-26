from django.urls import path
from .views import DashboardsView
from . import views

urlpatterns = [
    # Main dashboard page
    path(
        "",
        DashboardsView.as_view(template_name="dashboard_analytics.html"),
        name="index",
    ),

    # API endpoints for charts
    path('api/movies-over-time/', views.movies_over_time, name='movies_over_time'),
    path('api/genre-distribution/', views.genre_distribution, name='genre_distribution'),
    path('api/character-movie-counts/', views.character_movie_counts, name='character_movie_counts'),
    path('api/most-featured-strawhats/', views.most_featured_strawhats, name='most_featured_strawhats'),
]
