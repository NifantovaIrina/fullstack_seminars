from django.urls import path

# from tournaments.views import list_tournaments, tournament_info, create_tournament, add_battle, create_battle
from rest_framework.routers import DefaultRouter

from tournaments.views import TournamentViewSet

app_name = 'tournaments'

router = DefaultRouter()
router.register('', TournamentViewSet, basename='tournaments')
urlpatterns = router.urls