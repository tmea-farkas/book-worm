from django.db import models
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField
# Create your models here.

def def_image():
    return 'static/images/default-image.png'

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='profile')
    bio = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    profile_picture = CloudinaryField('image', default=def_image)


    def __str__(self):
        return str(self.user.username)
