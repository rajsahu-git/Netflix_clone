from django.urls import path
from .views import Home,Profiles,ProfileCreate, Watch, ShowMovieDetails, ShowMovie


app_name='app'

urlpatterns = [
    path("",Home.as_view(),name="home"),
    path("profile/",Profiles.as_view(),name="profile"),
    path("profileCreate/",ProfileCreate.as_view(),name="profileCreate"),
    path("watch/<str:profile_id>/",Watch.as_view(),name="watch"),
    path("movie_details/<str:movie_id>/",ShowMovieDetails.as_view(),name="show"),
    path('play/<str:movie_id>/',ShowMovie.as_view(),name="play")
]
