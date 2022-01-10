from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):
    """extends default create_user that takes email instead of username"""
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_employer = True
        user.is_superuser = True

        user.save(using=self._db)

        return user
class User(AbstractBaseUser, PermissionsMixin):
    username = None
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/users/')
    bio = models.TextField(blank=True)
    email = models.CharField(max_length=50, unique=True)
    is_employer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # username = models.CharField(default="", max_length=200, unique=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()


    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            new_url = "photos/users/" + str(self.photo)
            return new_url

    def __str__(self):
        return self.name
    

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    post_date = models.DateTimeField(default=datetime.now)
    like = models.ManyToManyField(User, related_name="user_likes")

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

