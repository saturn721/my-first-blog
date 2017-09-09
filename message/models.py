from django.db import models
from django.utils import timezone


# Create your models here.

class Ordering(models.Model):
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def send(self):
        self.created_date = timezone.now()
        self.save

    def __str__(self):
        return self.title
    """docstring for Ordering"""
    