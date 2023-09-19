from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError
import requests
from movies.models import Movies, People, MoviesPeople


class Command(BaseCommand):
    def handle(self, *args, **options):
        
        api_url = "https://kntk.de/kinode/movies"
        s = requests.Session()
        response = s.get(api_url)
        api_doc = response.json()

        for movie in api_doc['movies']:
            path = movie["path"]
            id = movie["id"]
            imdb_id = movie["imdb_id"]
            res = s.get(path)
            movie_doc = res.json()
            print(movie)

            original_title = movie_doc["original_title"]
            created_at = movie_doc["created_at"]
            poster_file_name = movie_doc["poster_url"]
            imdb_id = movie_doc["imdb_id"]
            photo_file_name = movie_doc["photo_url"]
            imdb_rating = movie_doc["imdb_rating"]
            genre = ','.join(map(str, movie_doc["genres"]))     
            spoken_languages = movie_doc["languages"]
            made_in = movie_doc["country"]
            spoken_languages = movie_doc["languages"]
            duration = movie_doc["duration"]
            popularity = movie_doc["popularity"]
            premiere_date = movie_doc["premiere_date"]
            summary = movie_doc["summary"]

            movie_obj, created = Movies.objects.update_or_create(
                original_title = original_title,
                defaults={
                    "stroer_id": id,
                    "created_at": created_at,
                    "poster_file_name": poster_file_name,
                    "imdb_id": imdb_id,
                    "photo_file_name": photo_file_name,
                    "imdb_rating": imdb_rating,
                    "genre": genre,
                    "spoken_languages": spoken_languages,
                    "made_in": made_in,
                    "duration": duration,
                    "popularity": popularity,
                    "premiere_date": premiere_date,
                    "summary": summary
                }
            )

            for p in movie_doc["people"]:
                people_id = p["id"]
                name = p["name"]
                role = p["role"]
                person_photo_file_name = p["photo"]
                character_name = ','.join(map(str, p["character_name"]))
                print(name)

                people_obj, created = People.objects.update_or_create(
                    name = name,
                )

                movie_people_obj, created = MoviesPeople.objects.update_or_create(
                    movie = movie_obj,
                    person = people_obj,

                    defaults={
                        "name": name,
                        "stroer_id": people_id,
                        "role": role,
                        "person_photo_file_name": person_photo_file_name,
                        "character_name": character_name
                    }
                )

               


