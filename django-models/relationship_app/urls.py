from django.urls import path
from .views import list_books

urlpatterns = [
    path('books/', views.list_view, name='list_books'),
    path('Library/', views.LibraryDetailView(), name='DetailView'),
]
