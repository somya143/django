from django.shortcuts import render,HttpResponse
from .models import Author,Contact
# Create your views here.
def onetoone(request):
    # author = Author.objects.create(name="Author 1")
    author = Author.objects.get(id=1)
    # Contact.objects.create(author=author, phone=85426266262)
    # contact = Contact.objects.get(id=1)
    return HttpResponse(author.contact.phone)
