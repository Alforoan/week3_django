from django.shortcuts import render, get_object_or_404
from .models import Author, Book
from django.http import HttpResponse

# print('AUTHOR OBJECTS ALL',Author.objects.all())
# print('BOOK OBJECTS ALL',Book.objects.all())
# author1_exists = Author.objects.filter(name='Harper Lee', date_of_birth='1926-04-28').exists()
# author1 = None
# author2 = None
# author3 = None
# if author1_exists:
#     print("Author 'Harper Lee' already exists.")
# else:
#     author1 = Author.objects.create(name='Harper Lee', date_of_birth='1926-04-28', biography='American novelist')

# author2_exists = Author.objects.filter(name='George Orwell', date_of_birth='1903-06-25').exists()
# if author2_exists:
#     print("Author 'George Orwell' already exists.")
# else:
#     author2 = Author.objects.create(name='George Orwell', date_of_birth='1903-06-25', biography='English novelist and essayist')


# author3_exists = Author.objects.filter(name='J.K. Rowling', date_of_birth='1965-07-31').exists()
# if author3_exists:
#     print("Author 'J.K. Rowling' already exists.")
# else:
#     author3 = Author.objects.create(name='J.K. Rowling', date_of_birth='1965-07-31', biography='British author, best known for the Harry Potter series')

# print('author1 exist',author1_exists)
# print('author2 exist',author2_exists)
# print('author3 exist', author3_exists)


# # Check if the book with ISBN '9780061120084' already exists
# book1_exists = Book.objects.filter(isbn='9780061120084').exists()
# # book1 = None
# # book2 = None
# # book3 = None
# if author1 and not book1_exists:
#     book1 = Book.objects.create(title='To Kill a Mockingbird', author=author1, summary='A novel by Harper Lee', isbn='9780061120084', genre='Fiction')
# else:
#     print("Book 'To Kill a Mockingbird' already exists.")
   
# # Check if the book with ISBN '9780451524935' already exists
# book2_exists = Book.objects.filter(isbn='9780451524935').exists()
# if author2 and not book2_exists:
#     book2 = Book.objects.create(title='1984', author=author2, summary='A dystopian novel by George Orwell', isbn='9780451524935', genre='Dystopian Fiction')
# else:
#     print("Book '1984' already exists.")

# # Check if the book with ISBN '9780590353427' already exists
# book3_exists = Book.objects.filter(isbn='9780590353427').exists()
# if author3 and not book3_exists:
#     book3 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author3, summary='The first book in the Harry Potter series', isbn='9780590353427', genre='Fantasy Fiction')
# else:
#     print("Book 'Harry Potter and the Philosopher's Stone' already exists.")



# author1 = Author.objects.create(name='Harper Lee', date_of_birth='1926-04-28', biography='American novelist')
# author2 = Author.objects.create(name='George Orwell', date_of_birth='1903-06-25', biography='English novelist and essayist')
# author3 = Author.objects.create(name='J.K. Rowling', date_of_birth='1965-07-31', biography='British author, best known for the Harry Potter series')
# book1 = Book.objects.create(title='To Kill a Mockingbird', author=author1, summary='A novel by Harper Lee', isbn='9780061120084', genre='Fiction')
# book2 = Book.objects.create(title='1984', author=author2, summary='A dystopian novel by George Orwell', isbn='9780451524935', genre='Dystopian Fiction')
# book3 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author3, summary='The first book in the Harry Potter series', isbn='9780590353427', genre='Fantasy Fiction')

# Create your views here.
def index(request):
    return HttpResponse('something is here')


def book_list(request):
    """
    View function for displaying a list of books.

    Returns:
        HttpResponse: A rendered HTML page displaying a list of books.
    """
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def author_list(request):
    """
    View function for displaying a list of authors.

    Returns:
        HttpResponse: A rendered HTML page displaying a list of authors.
    """
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def book_detail(request, pk):
    """
    View function for displaying details of a book.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the book.

    Returns:
        HttpResponse: A rendered HTML page displaying details of the book.
    """
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def author_detail(request, author_id):
    """
    View function for displaying details of an author.

    Args:
        request (HttpRequest): The HTTP request object.
        author_id (int): The primary key of the author.

    Returns:
        HttpResponse: A rendered HTML page displaying details of the author.
    """
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})