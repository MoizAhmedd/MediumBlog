from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length = 20)
    title = models.CharField(max_length = 200)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('home')
