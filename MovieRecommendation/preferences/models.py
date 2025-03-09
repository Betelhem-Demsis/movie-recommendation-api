from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    movie_id = models.IntegerField() 
    movie_title = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie_id') 

    def __str__(self):
        return f"{self.user.username} - {self.movie_title}"
