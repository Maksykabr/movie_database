from django.core.management.base import BaseCommand

from ...models import Director, Actor, Movie
from ...get_data import get_data, prepared_data


class Command(BaseCommand):
    help = 'Import movies from API'

    def handle(self, *args, **options):
        movies_list = get_data()
        prepared_movies_data = prepared_data(movies_list)
        print('server is in import movies')
        for movie_data in prepared_movies_data:
            print(movie_data)
            director_name = movie_data['director']
            director, _ = Director.objects.get_or_create(name=director_name)

            actors_data = movie_data['actors']
            actors = [Actor.objects.get_or_create(name=actor)[0] for actor in actors_data]

            movie, created = Movie.objects.get_or_create(
                title=movie_data['title'],
                release_year=movie_data['release_year'],
                director=director
            )
            movie.actors.set(actors)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully imported movie: {movie.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Movie already exists: {movie.title}"))

        self.stdout.write(self.style.SUCCESS("Movies import completed successfully"))