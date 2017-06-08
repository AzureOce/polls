from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    website = models.URLField()


class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=80)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publish_date = models.DateField()
