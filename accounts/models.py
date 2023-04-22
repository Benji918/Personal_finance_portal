from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
import random


# Create your models here.
class CustomUser(User):
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    #                              message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
    #                                      "allowed.")
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
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


class SMSCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    number = models.CharField(max_length=6, blank=False, null=False)

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        number_list = [num for num in range(10)]
        code_items = []

        for i in range(6):
            num = random.choice(number_list)
            code_items.append(num)
        code_string = ''.join(str(item) for item in code_items)
        self.number = str(code_string)

        super().save(*args, **kwargs)
