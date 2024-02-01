from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<movie_id>", views.movie, name="movie"),
    path("genre/<str:genre>", views.genres, name="genres"),
    path("mylist", views.mylist, name="mylist"),
    path("search", views.search, name="search"),
    path("person/", views.person, name="person"),
]