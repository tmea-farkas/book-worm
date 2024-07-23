from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Posted'))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(#one-to-many foreign key
        User, on_delete=models.CASCADE, related_name='bookworm_posts'
    )
    content = models.TextField() # post content
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)