from django.urls import path

from tournaments.views import list_tournaments, tournament_info, create_tournament, add_battle, create_battle

app_name = 'tournaments'

urlpatterns = [
    path('', list_tournaments, name='list'),
    path('<int:pk>/', tournament_info, name='info'),
    path('create/', create_tournament, name='create'),
    path('<int:pk>/add_batle/<int:battle_pk>', add_battle, name='add_battle'),
    path('<int:pk>/create_battle/', create_battle, name='create_battle')
]
