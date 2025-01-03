from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

class Contact(models.Model):
    address = models.CharField(default="Jagdalpur",max_length=300)
    phone = models.IntegerField()
    author = models.OneToOneField(Author,on_delete=models.CASCADE)
