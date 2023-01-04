from django.urls import path
from .views import Home,ProfileList,ProfileCreate,Watch,ShowMovieDetails,ShowMovie

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:profile_id>/',Watch.as_view(),name='watch'),
    path('movie/details/<str:movie_id>/',ShowMovieDetails.as_view(),name='show_det'),
    path('movie/play/<str:movie_id>/',ShowMovie.as_view(),name='play')
]