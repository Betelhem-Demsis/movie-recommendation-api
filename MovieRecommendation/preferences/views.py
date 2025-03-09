from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import FavoriteMovie
from .serializers import FavoriteMovieSerializer

class FavoriteMovieView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 10))  
    def get(self, request):
        favorites = FavoriteMovie.objects.filter(user=request.user)
        serializer = FavoriteMovieSerializer(favorites, many=True)
        return Response(serializer.data)

    def post(self, request):
        movie_id = request.data.get("movie_id")
        movie_title = request.data.get("movie_title")

        if not movie_id or not movie_title:
            return Response({"error": "movie_id and movie_title are required."}, status=status.HTTP_400_BAD_REQUEST)

        favorite, created = FavoriteMovie.objects.get_or_create(
            user=request.user,
            movie_id=movie_id,
            defaults={"movie_title": movie_title}
        )

        if not created:
            return Response({"message": "Movie is already in favorites."}, status=status.HTTP_200_OK)

        return Response({"message": "Movie added to favorites."}, status=status.HTTP_201_CREATED)

    def delete(self, request):
        movie_id = request.data.get("movie_id")
        if not movie_id:
            return Response({"error": "movie_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        favorite = FavoriteMovie.objects.filter(user=request.user, movie_id=movie_id).first()
        if not favorite:
            return Response({"error": "Movie not found in favorites."}, status=status.HTTP_404_NOT_FOUND)

        favorite.delete()
        return Response({"message": "Movie removed from favorites."}, status=status.HTTP_204_NO_CONTENT)
