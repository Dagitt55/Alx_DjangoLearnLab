# app/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from app.models import Book
from .form import ExampleForm

@permission_required('app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        pass
    return render(request, 'create_book.html')

@permission_required('app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
            return render(request, 'delete_book.html', {'book': book})
