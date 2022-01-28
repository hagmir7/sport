from random import randint
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='PostImage')
    tags = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title +'-'+ str(randint(1,1000)))
        super().save(*args, **kwargs)
