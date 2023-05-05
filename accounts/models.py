from django.utils import timezone
from django.conf import settings
from django.db import models
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
import random
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractUser
from django.utils.text import slugify


# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user manager that uses email as the unique identifier for authentication.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a new superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser should have is_staff as True'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser should have is_superuser as True'))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser should have is_active as True'))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    """
        Custom user model with email field as the unique identifier for authentication.
        """
    first_name = models.CharField(_('first name'), max_length=30, blank=False, null=False, unique=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=False, null=False, unique=True)
    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff status'), default=False)
    enable_two_factor_authentication = models.BooleanField(null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    # New fields for email verification
    email_verified = models.BooleanField(_('email verified'), default=False,
                                         help_text=_('Designates whether the user has verified their email.'))

    objects = CustomUserManager()

    # Set the email field as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.email.split('@')[0])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default='avatar.jpg',  # default avatar
        upload_to='profile_avatars'  # dir to store the image
    )
    bio = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @property
    def image_url(self):
        return (
            f"https://res.cloudinary.com/dfpsmxcgk/{self.avatar}"
        )

    # def save(self, *args, **kwargs):
    #     # save the profile first
    #     super().save(*args, **kwargs)
    #
    #     # resize the image
    #     img = Image.open(self.avatar.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         # create a thumbnail
    #         img.thumbnail(output_size)
    #         # overwrite the larger image
    #         img.save(self.avatar.path)


class SMSCode(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='smscode')
    number = models.CharField(max_length=6, blank=False, null=False)

    def __str__(self):
        return f'{self.user.username}-{self.number}'

    def save(self, *args, **kwargs):
        verification_code = random.randint(100000, 999999)
        self.number = str(verification_code)

        super().save(*args, **kwargs)


