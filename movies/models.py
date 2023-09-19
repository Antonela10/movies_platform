from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movies(models.Model):
    original_title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    poster_file_name = models.CharField(max_length=255, blank=True, null=True)
    imdb_id = models.CharField(max_length=255, blank=True, null=True)
    photo_file_name = models.CharField(max_length=255, blank=True, null=True)
    imdb_rating = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    spoken_languages = models.CharField(max_length=255, blank=True, null=True)
    made_in = models.CharField(max_length=255, blank=True, null=True)
    directors = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    popularity = models.DecimalField(max_digits=18, decimal_places=12, blank=True, null=True)
    premiere_date = models.DateTimeField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    stroer_id = models.IntegerField(blank=True, null=True)
    trailer_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.original_title
    
class People(models.Model):
    id = models.AutoField(primary_key=True)
    birthday = models.DateField(blank=True, null=True)
    deathday = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class MoviesPeople(models.Model):
    person = models.ForeignKey(
        People,
        on_delete=models.CASCADE,
        related_name="movie_people",
    )
    movie = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE,
        related_name="movie_people",
    )
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    person_photo_file_name = models.CharField(max_length=255, blank=True, null=True)
    character_name = models.CharField(max_length=255, blank=True, null=True)
    stroer_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class MoviesList(models.Model):
    movies_list = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="movies")
    movies_list_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movies_list_user")

    def __str__(self):
        return self.movies_list.original_title
