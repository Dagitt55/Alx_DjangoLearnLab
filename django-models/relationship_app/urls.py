from django.urls import path
from .views import list_books

urlpatterns = [
    path('list_books/', views.list_view, name='list_books'),
    path('LibraryDetailView/', views.LibraryDetailView(), name='DetailView'),
]
