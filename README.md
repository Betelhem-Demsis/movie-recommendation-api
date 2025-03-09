### 📌 Overview
The **Movie Recommendation App** is a Django-based REST API that allows users to search for movies, view details and recommendations and manage their favorite movies. The app integrates with an external movie database (TMDB API) to fetch movie details.

### 🚀 Features
- **User Authentication**: Register, login, and manage user accounts.
- **Movie Details**: View movie information, including recommendations.
- **Favorites**: Add and remove movies from favorites.

## 🛠️ Tech Stack
- **Backend**: Django, Django REST Framework (DRF)
- **External API**: TMDB API (for movie data)
- **Authentication**: Token-based authentication


## 🔗 API Endpoints
### **Authentication**
- `POST /api/accounts/register/` → Register a new user
- `POST /api/accounts/login/` → Login and receive a token
- `POST /api/accounts/logout/` → Logout user

### **Movies**
- `GET /api/movies/movie-list/` → popular a movie
- `GET /api/movies/movie/<movie_id>/` → Get movie details and recommendations


### **Favorites**
- `GET /api/preference/favorites/` → View favorite movies
- `POST /api/preference/favorites/` → Add a movie to favorites
- `DELETE /api/preference/favorites/` → remove a movie from favorites



