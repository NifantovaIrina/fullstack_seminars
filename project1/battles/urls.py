from django.urls import path

from battles.views import list_battles, create_battle

app_name = 'battles'

urlpatterns = [
    path('', list_battles, name='list'),
    # path('<int:pk>/', tournament_info, name='info'),
    path('create/', create_battle, name='create')
]