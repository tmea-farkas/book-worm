from django.db import models
import uuid
from profiles.models import Profile
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Posted'))

def_image = "{% url 'static/images/logo.png' %}"
Book = 'Book'

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
    description = models.TextField()
    cover_photo = CloudinaryField('image', default=def_image)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

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
    genre = models.CharField(max_length=100, verbose_name='genre', help_text="Enter the books' genre.")
    sub_genre = models.TextField(verbose_name='sub-genre', help_text='Enter the sub-genre this book falls under.')

    def __str__(self):
        return self.name
