from django_filters import rest_framework as filters

from .models import Movie


class MovieFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    release_year = filters.NumberFilter()
    director__name = filters.CharFilter(lookup_expr='icontains')
    actors__name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['name', 'release_year', 'director__name', 'actors__name']