from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length = 20)
    title = models.CharField(max_length = 200)
    text = models.TextField()

