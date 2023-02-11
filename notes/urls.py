from django.urls import path
from . import views

urlpatterns = [
    path('getAll/', views.getAllTheNotes),
    path('add/', views.addNote),
    path('get/', views.getNote),
    path('update/', views.updateNote),
    path('delete/', views.deleteNote),
    path('deleteAll/', views.deleteAllTheNotes),
    path('register/', views.register),
    path('login/', views.login)
]