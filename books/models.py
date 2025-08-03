from django.contrib import admin
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    contact_number = models.PositiveBigIntegerField(unique=True)
    #contact_number = models.TextField(max_length=12, null=True, blank=True)
    biography = models.TextField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    tittle = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    isbn = models.TextField(max_length=30, unique=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle
