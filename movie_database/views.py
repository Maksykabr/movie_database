from django.shortcuts import render
from django.views import View

from .filters import MovieFilter
from .paginations import MyPagination

from rest_framework import mixins, viewsets

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
    pagination_class = MyPagination


class ActorViewsSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = MyPagination


class MovieViewsSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MyPagination


class MovieFilterViewsSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        context = {'movies': serializer.data}
        return render(request, 'movie_database/filter_page.html', context)


class PreviewView(View):
    template_name = 'movie_database/preview.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
