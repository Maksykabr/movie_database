from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from .management.commands.import_movies import Command as ImportMoviesCommand

from rest_framework import mixins, viewsets

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet

from .models import Director, Actor, Movie
from .serializers import DirectorSerializer, ActorSerializer, MovieSerializer


class DirectorViewsSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ActorViewsSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewsSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MoviesViewsSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['release_year', 'director__name', 'actors__name']


@method_decorator(csrf_exempt, name='dispatch')
class ImportMoviesViewSet(GenericViewSet):
    @action(detail=False, methods=['post'])
    def import_movies(self, request):
        command = ImportMoviesCommand()
        command.handle()
        return JsonResponse({'status': 'success', 'message': 'Movies imported successfully'})
