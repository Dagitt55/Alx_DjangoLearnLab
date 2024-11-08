from django.shortcuts import render

from .models import Book

def list_books(request):
	books = Book.objects.all()
	context = {'list_books': books}
	return render(request, "relationship_app/list_books.html", "Book.objects.all()")
