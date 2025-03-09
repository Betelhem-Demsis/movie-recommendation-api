from django.urls import path
from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('movie-list/', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:movie_id>/', MovieDetailView.as_view(), name='movie_detail'),
]