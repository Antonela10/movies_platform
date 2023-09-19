from django.contrib import admin
from django.utils.html import format_html
from django.template.defaultfilters import mark_safe

from .models import *

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    search_fields = ['original_title']


class PeopleAdmin(admin.ModelAdmin):
    
    search_fields = ['name']
    fields = ('name', 'movies')

    readonly_fields = ('movies',)

    def movies(self, obj):
        return format_html(
            '<a href="/admin/movies/moviespeople/?person_id=%s">%s</a>'
            % (obj.id, obj.movie_people.all().count())
        )

    movies.short_description = mark_safe("<strong>Movie people</strong>")  
    movies.allow_tags = True

    # list_display = ["name", "display_related_movies"]

    # def display_related_movies(self, obj):
    #     # Retrieve all the movies related to the current person
    #     related_movies = obj.movie_people.all()

    #     # Create a comma-separated string of movie names
    #     movie_names = ", ".join([movie.movie.original_title for movie in related_movies])

    #     return movie_names

    # display_related_movies.short_description = 'Related Movies'

   

class MoviesPeopleAdmin(admin.ModelAdmin):
    search_fields = ['name']
	
admin.site.register(Movies, MoviesAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(MoviesPeople, MoviesPeopleAdmin)
admin.site.register(MoviesList)