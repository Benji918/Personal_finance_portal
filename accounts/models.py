from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

# Create your models here.
# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default='avatar.jpg',  # default avatar
        upload_to='profile_avatars'  # dir to store the image
    )
    bio = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)

# Account activation
# class CustomUser(BaseUserManager):
#     activation_key = models.CharField(max_length=40, blank=True)
#     key_expires = models.DateTimeField(default=timezone.now)
#
#     def activate(self, key):
#         if self.activation_key == key and timezone.now() <= self.key_expires:
#             self.is_active = True
#             self.activation_key = ''
#             self.key_expires = None
#             self.save()
#             return True
#         return False
