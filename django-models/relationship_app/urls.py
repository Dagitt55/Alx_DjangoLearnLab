from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.hello_view, name='book_list'),
    path('about/', views.AboutView.as_view(), name='about'),
]
