from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
import os

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library_manager/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library_manager/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            if 'image' in request.FILES or 'image-clear' in request.POST:
                if book.image:
                    if os.path.isfile(book.image.path):
                        os.remove(book.image.path)
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library_manager/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library_manager/book_confirm_delete.html', {'book': book})