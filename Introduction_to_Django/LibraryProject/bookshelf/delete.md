# Delete Operation

# python command
"from bookshelf.models import Book"
book.delete()
all_books_after_delete = Book.objects.all()
print(all_books_after_delete)

# Expected Output: <QuerySet []>
