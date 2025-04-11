from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.character_list, name='character_list'),
    path('battle/<int:attacker_id>/<int:defender_id>/', views.battle_view, name='battle_view'),
]