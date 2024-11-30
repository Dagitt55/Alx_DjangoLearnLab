# API Endpoints

## GET /api/books/
- Retrieves all books.
- Public access (read-only).

## GET /api/books/<int:pk>/
- Retrieves a single book by ID.
- Public access (read-only).

## POST /api/books/create/
- Creates a new book.
- Requires authentication.

## PUT /api/books/<int:pk>/update/
- Updates an existing book.
- Requires authentication and permission to edit the book.

## DELETE /api/books/<int:pk>/delete/
- Deletes a book.
- Requires authentication and permission to delete the book.
