from django.db import models

# Create your models here.

# one to one relationship
class Author(models.Model):
    name = models.CharField(max_length=200)

class Contact(models.Model):
    address = models.CharField(default="Jagdalpur",max_length=300)
    phone = models.IntegerField()
    author = models.OneToOneField(Author,on_delete=models.CASCADE)

# one to many relationship
class Article(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(default='No description required')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='articles')

# many to many relationship
class Courses(models.Model):
    title = models.CharField(max_length=400)

class Students(models.Model):
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(Courses,related_name='students')
