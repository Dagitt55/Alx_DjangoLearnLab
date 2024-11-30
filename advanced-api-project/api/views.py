from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter, NumberFilter
from rest_framework.filters import OrderingFilter



# Book List View with filtering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title or publication_year
    ordering = ['title']  # Default ordering by title

# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow unauthenticated read-only access

# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books

# Custom filter class for the Book model
class BookFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='Title')
    author = CharFilter(lookup_expr='icontains', label='Author')
    publication_year = NumberFilter(lookup_expr='exact', label='Publication Year')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


# Allows users to filter books by title, author, and publication year.
filterset_class = BookFilter

# Enables searching by title and author fields.
search_fields = ['title', 'author']

# Allows users to order books by title or publication year.
ordering_fields = ['title', 'publication_year']
ordering = ['title']  # Default ordering by title
