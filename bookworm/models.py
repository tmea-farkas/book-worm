from django.db import models
import uuid
from profiles.models import Profile
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Posted'))

def_image = "{% url 'static/images/logo.png' %}"
Book = 'Book'
Genre = 'Genre'
#Comment model
class Comment(models.Model):
    post = models.ForeignKey(
        Book, on_delete=models.CASCADE, name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, name='commenter'
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

# The book model
class Book(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    cover_photo = CloudinaryField('image', default=def_image)
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Profile, related_name='book_likes')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def __str__(self):
        return self.genre

    def total_likes(self):
        return self.likes.count()

    def get_likes(self):
        return self.likes_set.all()

# Book rating model
class Rating(models.Model):
    book = models.ForeignKey(Book, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f'{self.book.title} - {self.rating}'

# Genre model
class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='genre',
        help_text="Enter the books' genre.")

    def __str__(self):
        return self.name
