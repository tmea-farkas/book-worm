from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Rating, Profile
from django.contrib.auth.decorators import login_required
from .forms import RatingForm, BookForm

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        context = {'profile': profile}
    else:
        context = {}
    return render(request, 'home.html/', context)


@login_required
def new_book(request):
    profile = get_object_or_404(Profile, user=request.user)
    form = BookForm(request.POST)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = profile
            book.save()
            messages.success(request, 'Your book was added successfully!')
    return render(request, 'add_book.html/', context)

@login_required
def addPost(request):
    profile - get_object_or_404(Profile, user=request.user)
    form = PostForm(request.POST)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = post.save(commit=False)
            post.owner = profile
            post.save()
            messages.success(request, 'Your post was shared successfully!')
    return render(request, 'new_post.html', context)



@login_required
def deleteBook(request, pk):
    user = get_object_or_404(Profile, user=request.user)
    book = get_object_or_404(Book, id=pk)
    if book.reader == user:
        book.delete()
        message.success(request, 'This book is now deleted!')
        return redirect('home')
    context = {'object': book}
    return render(request, 'bookworm/books.html', context)



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
