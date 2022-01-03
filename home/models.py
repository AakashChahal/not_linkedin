from django.db import models
from datetime import datetime

class User(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=f'photos/users/')
    bio = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    is_employer = models.BooleanField(default=False)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.name
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    post_date = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField()

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

