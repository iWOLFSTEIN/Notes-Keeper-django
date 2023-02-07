from django.urls import path
from . import views

urlpatterns = [
    path('allrecords/', views.getAllTheNotes),
    path('add/', views.addNote),
    path('get/', views.getNote)
]