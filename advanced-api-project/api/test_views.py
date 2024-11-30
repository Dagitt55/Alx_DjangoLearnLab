from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create an author for testing
        cls.author = Author.objects.create(name="J.K. Rowling")
        
        # Create some book instances
        cls.book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", 
                                        publication_year=1997, author=cls.author)
        cls.book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", 
                                        publication_year=1998, author=cls.author)

        # Create a test user for authenticated access
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
    
    # Test: Retrieve all books (ListView)
    def test_book_list(self):
        url = '/books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two books created
    
    # Test: Retrieve a single book (DetailView)
    def test_book_detail(self):
        url = f'/books/{self.book1.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
    
    # Test: Create a new book (CreateView)
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        url = '/books/'
        data = {
            'title': 'Harry Potter and the Prisoner of Azkaban',
            'publication_year': 1999,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
    
    def test_create_book_unauthenticated(self):
        url = '/books/'
        data = {
            'title': 'Harry Potter and the Goblet of Fire',
            'publication_year': 2000,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    # Test: Update an existing book (UpdateView)
    def test_update_book(self):
        self.client.login(username='testuser', password='testpassword')
        url = f'/books/{self.book1.id}/'
        data = {'title': 'Updated Title', 'publication_year': 1998, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')
    
    # Test: Delete a book (DeleteView)
    def test_delete_book(self):
        self.client.login(username='testuser', password='testpassword')
        url = f'/books/{self.book1.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Only 1 book should remain
    
    # Test: Filtering by title
    def test_filter_by_title(self):
        url = '/books/?title=Harry Potter'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books contain "Harry Potter" in their title
    
    # Test: Searching by author
    def test_search_by_author(self):
        url = '/books/?search=Rowling'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books are by "J.K. Rowling"
    
    # Test: Ordering by publication year
    def test_ordering_by_year(self):
        url = '/books/?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)  # The first book should have the earliest year
    
    # Test: Unauthorized access for delete operation
    def test_unauthorized_delete(self):
        url = f'/books/{self.book1.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
