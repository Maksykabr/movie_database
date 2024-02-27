from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'directors', views.DirectorViewsSet)
router.register(r'actors', views.ActorViewsSet)
router.register(r'movie', views.MovieViewsSet)
router.register(r'movies', views.MoviesViewsSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
