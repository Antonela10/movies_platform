from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.urls import reverse
from django.contrib import messages
import random
import json

from .models import Movies, MoviesList, MoviesPeople, People
from django.contrib.auth.models import User

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    movies = Movies.objects.all()[:15]
    most_popular_movies = Movies.objects.all().order_by('-popularity')[:15]
    latest_movies = Movies.objects.all().order_by('-created_at')[:15]
    
    # Collect all genres for movies and store them in a unique list
    all_genres = []
    unique_genres = []
    for movie in movies:
        movie_genre = movie.genre
        all_genres.append(movie_genre)
        split_genres_list = [genres.split(',') for genres in all_genres]
        flattened_list = [item for sublist in split_genres_list for item in sublist]
        unique_genres = sorted(list(set(filter(None, flattened_list))))

    random_genre = random.choice(unique_genres)
    random_genre_movies = Movies.objects.all().filter(genre = random_genre)[:15]
       
    return render(request, 'movies/index.html', {
        "movies": movies,
        "most_popular_movies": most_popular_movies,
        "latest_movies": latest_movies,
        "all_genres": all_genres,
        "random_genre": random_genre,
        "random_genre_movies": random_genre_movies
    })

def genres(request, genre):
    movies = Movies.objects.all()
    movies_by_genres = []
    for movie in movies:
        movie_genre = movie.genre.split(',')
        if genre in movie_genre:
            movies_by_genres.append(movie)

    # Set up Paginaton
    p = Paginator(movies_by_genres, 45)
    page = request.GET.get("page")
    movies_by_genres = p.get_page(page)

    return render(request, 'movies/genres.html', {
        "genre": genre,
        "movies_by_genres": movies_by_genres
    })

def movie(request, movie_id):
    movie = Movies.objects.get(pk = movie_id)
    movie_people = movie.movie_people.all()

    movie_genre = movie.genre
    genre_list = [genre.strip().title() for genre in movie_genre.split(",")]

    # Extract directors, producers and actors names
    directors = movie.movie_people.all().filter(role = 'director')
    producers = movie.movie_people.all().filter(role = 'producer')
    actors = movie.movie_people.all().filter(role = 'actor')
   
    # Collect id's of movies in My List
    mylist_user = request.user.id
    mylist_movies_ids = []
    my_movies_list = MoviesList.objects.filter(movies_list_user=mylist_user)
    for my_movie in my_movies_list:
        mylist_movies_ids.append(my_movie.movies_list.stroer_id)

    # Movie duration
    durration_only_minutes = int(movie.duration)
    hours = durration_only_minutes // 60
    minutes = durration_only_minutes % 60
    movie_duration = f'{hours}h {minutes}min'

    

    return render(request, 'movies/movie.html', {
        "movie": movie,
        "genre_list": genre_list,
        "movie_people": movie_people,
        "directors": directors,
        "producers": producers,
        "actors": actors,
        "movie_duration": movie_duration,
        "mylist_movies_ids": mylist_movies_ids,
    })

# Add movies to My List
def mylist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            me = request.user.id
            movie_list_user = User.objects.get(pk=me)
            action = request.POST.get("action", None)

            if action == "add":
                movie_id = int(request.POST.get("movie_id", False))
                movie = Movies.objects.get(stroer_id=movie_id)
                mylist_item = MoviesList.objects.create(movies_list_user=movie_list_user, movies_list=movie)
                mylist_item.save()

            elif action == "remove":
                movie_id = int(request.POST.get("movie_id", False))
                MoviesList.objects.filter(movies_list_user = movie_list_user, movies_list__stroer_id = movie_id).delete()
            
            my_movies_list = MoviesList.objects.filter(movies_list_user=movie_list_user)
            return HttpResponseRedirect(reverse ('mylist'))

    else:
        if request.user.is_authenticated:
            movie_list_user = request.user.id
            my_movies_list = MoviesList.objects.filter(movies_list_user=movie_list_user)
            return render(request, 'movies/mylist.html', {
                "my_movies_list": my_movies_list,
                "message": "Your Movies List Is Empty",
                
            })

    return render(request, 'movies/mylist.html', {
        "my_movies_list": my_movies_list,
    })



def search(request):
    if request.method == "POST":
        searched = request.POST["search"]
        searched_movie = Movies.objects.filter(original_title__icontains=searched)
        searched_movies = searched_movie.order_by("-popularity").all()

        print(searched_movies)
        return render(request, "movies/search.html", {
            "searched": searched,
            "searched_movies": searched_movies,
        })

    else:
        return render(request, 'auctions/search_listing.html', {})
    

def person(request):
    person_movies = []
    person_roles = set()

    if request.method == "GET":
        person_id = request.GET.get('person_id')
        try:
            person = People.objects.get(id = person_id)
            try:
                movies_people_instances = person.movie_people.all()
                for movies_people_instance in movies_people_instances:
                    person_photo_file_name = movies_people_instance.person_photo_file_name 
                    person_roles.add(movies_people_instance.role.capitalize())
                    person_movies.append(movies_people_instance.movie.original_title)
                    
            except MoviesPeople.DoesNotExist:
                movies_people_instances = []
               
            additional_info = {
                'name': person.name,
                'person_photo_file_name': person_photo_file_name,
                'person_roles': list(person_roles),
                'person_movies': person_movies
            }
            return JsonResponse(additional_info)
        except People.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "movies/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "movies/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # Check if any of the fields are empty
        if not username or not email or not password or not confirmation:
            return render(request, "movies/register.html", {
                "message": "All fields must be filled out."
            })

        # Ensure password matches confirmation
        if password != confirmation:
            return render(request, "movies/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "movies/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "movies/register.html")
       