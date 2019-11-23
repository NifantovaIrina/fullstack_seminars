from django.urls import path
from rest_framework.routers import DefaultRouter

from battles.views import BattleViewSet

app_name = 'battles'
router = DefaultRouter()
router.register('', BattleViewSet, basename='battles')
urlpatterns = router.urls