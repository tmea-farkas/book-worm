from django.db import models
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField
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
    edited_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    exerpt = models.TextField(blank=True)

#class Profile(models.Model):
 #   id = models.UUIDField(unique=True,
 #                         primary_key=True,
  #                        editable=False,
   #                       default=uuid.uuid4)
   # user = models.ForeignKey(User,
    #                         blank=False,
     #                        null=False,
      #                       related_name='profile',
       #                      on_delete=models.CASCADE)
    #profile_picture = CloudinaryField(
     #   'image',
      #  default=(#insert cloudinary default image)
    #),
     #   store='#folder where profile images are stored#' ,
      #  allowed_formats=['jpg', 'jpeg', 'png', 'webp'],
       # display={'width':120,
        #         'height':180,
         #        'format': 'png',
          #       'crop': 'fill',
           #      'quality': 'auto:good'},
        #bio = models.TextField()
    #)