from django.urls import path
from .views import list_books

urlpatterns = [
    path('book_list/', views.hello_view, name='book_list'),
    path('about/', views.AboutView.as_view(), name='about'),
]
