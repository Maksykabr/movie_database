# urls.py
from django.urls import path
from .views import DirectorList, ActorList, MovieList

urlpatterns = [
    path('directors/', DirectorList.as_view(), name='director-list'),
    path('actors/', ActorList.as_view(), name='actor-list'),
    path('movies/', MovieList.as_view(), name='movie-list'),
]
