from django.urls import path
# this imports all the views from the views.py
from . import views

urlpatterns = [
    # this is the home url
    path('cards/', views.cards, name='cards'),
    # this is the single card url
    path('card-detail/<str:id>/', views.card_detail, name='card-detail'),
    # this is the add card url
    path('add-card/', views.add_card, name='add-card'),
    # this is the edit card url
    path('edit-card/<str:id>/', views.edit_card, name='edit-card'),
    # this is the delete card url
    path('delete-card/<str:id>/', views.delete_card, name='delete-card'),
    path('matirial/', views.matirial, name='matirial'),
    path('projects/', views.projects, name='projects'),
    path('', views.home, name='home'),
]
