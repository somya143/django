from django.shortcuts import render,HttpResponse
from .models import Author,Contact,Article,Students,Courses
# Create your views here.
def onetoone(request):
    # author = Author.objects.create(name="Author 1")
    # author = Author.objects.get(id=1)
    # Contact.objects.create(author=author, phone=85426266262)
    # contact = Contact.objects.get(id=1)
    # one to manuy
    # Article.objects.create(author=author,title='Life of a trader', description="It is not easy")

    # # many to many
    # student1 = Students.objects.create(name='Student 1')
    # student2 = Students.objects.create(name='Student 2')
    # course1 = Courses.objects.create(title='Python Django course')
    # course2 = Courses.objects.create(title='python flask course')
    student1 = Students.objects.get(id=1)
    student2 = Students.objects.get(id=2)
    course1 = Courses.objects.get(id=2)
    course2 = Courses.objects.get(id=1)
    # course1.students.add(student1)
    # course2.students.add(student1)
    return HttpResponse(course2.students.all()[0].name)
