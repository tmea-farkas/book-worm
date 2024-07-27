from django.db import models
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField
# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Posted'))

placeholder = 'static/images/default_image.png'

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False, related_name='profile')
    username = models.CharField(max_length=30, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    profile_picture = CloudinaryField('image', default='placeholder')


    def __str__(self):
        return str(self.user.username)


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

