from .models import Movies

def genres_list(request):
    movies = Movies.objects.all()
    all_genres = []
    unique_genres = []
    for movie in movies:
        movie_genre = movie.genre
        all_genres.append(movie_genre)
        split_genres_list = [genres.split(',') for genres in all_genres]
        flattened_list = [item for sublist in split_genres_list for item in sublist]
        unique_genres = sorted(list(set(filter(None, flattened_list))))
    return {
        "unique_genres": unique_genres
    }