from django.db import models
from django.utils import timezone
import re
from django import forms
from django.db import models



# Create your models here.

class Ordering(models.Model):
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=200)
    message = models.TextField()
    age = models.PositiveIntegerField(default=18)
    eye_color = models.CharField(max_length=7, default='#000000')
    rice = models.CharField(max_length=6)
    boobs = models.PositiveIntegerField(default=3)
    waist = models.PositiveIntegerField(default=40)
    hair_color = models.CharField(max_length=7, default='#000000')
    taz = models.PositiveIntegerField( default=60)
    foot = models.PositiveIntegerField(default=30)
    created_date = models.DateTimeField(default=timezone.now)

    def send(self):
        self.created_date = timezone.now()
        self.save(update_fields=None)

    def __str__(self):
        return self.title
    """docstring for Ordering"""
    