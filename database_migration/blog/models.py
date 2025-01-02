from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default="No Content provided")
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Employees(models.Model):
    name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)