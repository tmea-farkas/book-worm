from django.db import models
import uuid
from profiles.models import Profile
from cloudinary.models import CloudinaryField
# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Posted'))

def def_image():
    return 'staticfiles/images/default-image.png'


#Post model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(#one-to-many foreign key
        User, on_delete=models.CASCADE, related_name='bookworm_posts'
    )
    content = models.TextField() # post content
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    exerpt = models.TextField(blank=True)


# The book model
class Book(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

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
