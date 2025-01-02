from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return 'success'
    else:
        form = RegisterForm()
    return render(request,"myforms/register.html",{"form":form})