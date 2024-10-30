from django.shortcuts import render,redirect
from books_authors_app.models import Book, Author

def view_books(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})
def view_book(request, id):
    book = Book.objects.get(id=id)
    authors = Author.objects.all()
    request.session['book'] = book.id
    return render(request, 'view_book.html', {'book': book, 'authors': authors})
def add_book(request):
    if len(request.POST['title']) < 1 or len(request.POST['desc']) < 1:
        return redirect('/')
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')
def view_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})
def view_author(request, id):
    author = Author.objects.get(id=id)
    books = Book.objects.all()
    request.session['author'] = author.id
    return render(request, 'view_author.html', {'author': author, 'books': books})
def add_author(request):
    if len(request.POST['first_name']) < 1 or len(request.POST['last_name']) < 1 or len(request.POST['notes']) < 1:
        return redirect('/authors')
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')
def assign_author(request):
    book_id = int(request.session['book'])
    if request.POST['author'] == 'none':
        return redirect(f'/books/{book_id}')
    author_id = int(request.POST['author'])
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=author_id)
    book.authors.add(author)
    return redirect(f'/books/{book_id}')
def assign_book(request):
    author_id = int(request.session['author'])
    if request.POST['book'] == 'none':
        return redirect(f'/authors/{author_id}')
    book_id = int(request.POST['book'])
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=author_id)
    author.books.add(book)
    return redirect(f'/authors/{author_id}')