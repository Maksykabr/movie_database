from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'directors', views.DirectorViewsSet, basename='directors')
router.register(r'actors', views.ActorViewsSet, basename='actors')
router.register(r'movies', views.MovieViewsSet, basename='movies')
router.register(r'movie_filter', views.MovieFilterViewsSet, basename='movies_filter')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/movie-filter/', views.MovieFilterViewsSet.as_view({'get': 'list'}), name='movie-filter-view'),
    path('', views.PreviewView.as_view(), name='home')
]
