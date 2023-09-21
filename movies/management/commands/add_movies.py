from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError
import requests
from movies.models import Movies, People, MoviesPeople


class Command(BaseCommand):
    def handle(self, *args, **options):
        
        # api_url = "https://kntk.de/kinode/movies"
        # s = requests.Session()
        # response = s.get(api_url)
        # api_doc = response.json()

        movies = Movies.objects.all()

        for movie in movies:
            path =  f"https://kntk.de/kinode/movies/{movie.stroer_id}"
            s = requests.Session()
            res = s.get(path)
            movie_doc = res.json()
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
                    movie = movie,
                    person = people_obj,

                    defaults={
                        "name": name,
                        "stroer_id": people_id,
                        "role": role,
                        "person_photo_file_name": person_photo_file_name,
                        "character_name": character_name
                    }
                )

               


