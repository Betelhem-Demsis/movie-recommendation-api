from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .utils import get_tmdb_data


class MovieListView(APIView):
    permission_classes = [permissions.IsAuthenticated] 

    def get(self, request):
        popular_movies = get_tmdb_data('movie/popular', {'language': 'en-US', 'page': 1})
        return Response({'movies': popular_movies.get('results', [])})


class MovieDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]  

    def get(self, request, movie_id):
        movie = get_tmdb_data(f"movie/{movie_id}", {'language': 'en-US'})
        recommendations = get_tmdb_data(f"movie/{movie_id}/recommendations", {'language': 'en-US'})

        return Response({
            'movie': movie,
            'recommendations': recommendations.get('results', [])
        })
