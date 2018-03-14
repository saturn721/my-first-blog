from django.db import models
from django.utils import timezone
import re
from django import forms
from django.db import models

# Create your models here.
class Entering(models.Model):
    title = 'enter'
    token = models.CharField(max_length=50)

    def send(self):
        self.created_date = timezone.now()
        self.save(update_fields=None)

    def __str__(self):
        return self.title
