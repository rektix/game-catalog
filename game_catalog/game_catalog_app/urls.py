from django.urls import path
from . import views

app_name = 'game_catalog_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),
    path('games/', views.games, name='games'),
    path('games/<int:id>/', views.game, name='game'),
    path('game/edit/<int:id>/', views.edit, name='edit'),
    path('game/new/', views.new, name='new'),
    path('game/comment/<int:id>', views.comment, name='comment')
]
