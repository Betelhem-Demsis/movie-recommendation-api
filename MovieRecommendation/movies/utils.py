import requests
from django.conf import settings

def get_tmdb_data(endpoint, params=None):
    base_url = "https://api.themoviedb.org/3"
    image_base_url = "https://image.tmdb.org/t/p/w500"  
    params = params or {}
    params['api_key'] = settings.TMDB_API_KEY
    response = requests.get(f"{base_url}/{endpoint}", params=params)
    data = response.json()
    
    if 'results' in data:
        for movie in data['results']:
            if 'poster_path' in movie:
                movie['poster_url'] = f"{image_base_url}{movie['poster_path']}"
            if 'original_name' in movie:
                movie['name'] = movie['original_name']
            if 'popularity' in movie:
                movie['popularity'] = round(movie['popularity'], 1)
            if 'vote_average' in movie:
                movie['vote_average'] = round(movie['vote_average'], 1)
            if 'vote_count' in movie:
                movie['vote_count'] = round(movie['vote_count'], 1)
    return data