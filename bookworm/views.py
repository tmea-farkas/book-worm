from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Rating, Profile
from django.contrib.auth.decorators import login_required
from .forms import RatingForm, BookForm
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Count

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        context = {'profile': profile}
    else:
        context = {}
    return render(request, 'bookworm/home.html', context)

def top_10(request):
    book_list = Book.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:10]
    for book in book_list:
        print(book.id)
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        context = {
            'profile': profile,
            'books': book_list,
        }
    else:
        context = {
            'books': book_list,
        }
    return render(request, 'top-10.html', context)

def genres(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        context = {'profile': profile}
    else:
        context = {}
    return render(request, 'genres.html', context)

def contact(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        context = {'profile': profile}
    else:
        context = {}
    return render(request, 'contact.html', context)

def viewBook(request, pk):
    book = get_object_or_404(Book, id=pk)
    context = {
        'book': book
    }
    return render(request, 'bookworm/book_display.html/', context)

@login_required
def new_book(request):
    profile = get_object_or_404(Profile, user=request.user)
    form = BookForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = profile
            book.save()
            messages.success(request, 'Your book was added successfully!')
            return redirect('home')
    return render(request, 'add_book.html/', context)


@login_required
def deleteBook(request, pk):
    user = get_object_or_404(Profile, user=request.user)
    book = get_object_or_404(Book, id=pk)
    if book.owner == user:
        book.delete()
        message.success(request, 'This book is now deleted!')
        return redirect('home')
    context = {'object': book}
    return render(request, 'bookworm/books.html', context)

#Book rating
@login_required
def rateBook(request, book_id):
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
        form = RatingForm(instance=rating)

    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'rate_book.html', context)

@login_required
def likeBook(request, pk):
    book = get_object_or_404(Book, id=request.POST.get('book_id'))
    profile = get_object_or_404(Profile, user=request.user)
    liked = False
    favourited = False
    if book.likes.filter(id=profile.id).exists():
        if book.favourites.filter(id=profile.id).exists():
            book.favourites.remove(profile.id)
            favourited = False
        book.likes.remove(profile.id)
        liked = False
    else:
        book.likes.add(profile.id)
        liked = True
        favourited = False

    if request.htmx:
        total_likes = book.total_likes()
        context = {
            'book': book,
            'total_likes': total_likes,
            'liked': liked,
            'favourited': favourited,
        }
        headers = {
            'HX-Trigger': 'liked',
        }
        return render(request, 'templates/bookworm/like_books.html/', context, headers)
    return HttpResponseRedirect(reverse('view-book', args=[str(pk)]))