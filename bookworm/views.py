from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Rating
from django.contrib.auth.decorators import login_required
from .forms import RatingForm, BookForm

# Create your views here.

def home(request):
    return render(request, 'bookworm/home.html')

def new_book(request, pk):
    book = Book.objects.get(id=pk)
    context = {'book': book}
    return render(request, 'bookworm/add_book.html', context)

#Book rating
@login_required
def rate_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    rating = Rating.objects.filter(book=book, user=request.user).first()

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.book = book
            new_rating.user = request.user
            new_rating.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form - RatingForm(instance=rating)

    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'rate_book.html', context)
