from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=40)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
