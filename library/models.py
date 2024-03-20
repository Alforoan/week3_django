from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=101)
    date_of_birth = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        #something
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    summary = models.TextField(blank=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.CharField(max_length=100, blank=True, help_text='Enter a book genre (e.g. Science Fiction, Romance)')

    def __str__(self):
        return self.title