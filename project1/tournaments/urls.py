from django.urls import path

from tournaments.views import list_tournaments, tournament_info, create_tournament

app_name = 'tournaments'

urlpatterns = [
    path('', list_tournaments, name='list'),
    path('<int:pk>/', tournament_info, name='info'),
    path('create/', create_tournament, name='create')
]
