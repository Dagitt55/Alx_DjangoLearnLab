from django.db import models

class Author(models.Model):
    """
    Author model to store details about an author.
    The name field stores the author's name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model to store details about a book.
    The title field stores the title of the book.
    The publication_year field stores the year of publication.
    The author field is a foreign key linking the book to an author (one-to-many relationship).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title