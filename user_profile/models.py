from django.db import models
from django.contrib.auth.models import User
from post.models import Post

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=user_directory_path,blank=True, null=True, default="default.jpg")
    favourite = models.ManyToManyField(Post, blank=True)

    