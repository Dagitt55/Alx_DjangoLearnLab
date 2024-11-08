from django.urls import path
from .views import list_books
from . import views
from django.contrib.auth.views import LoginView
from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
]
