from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("login")
        return render(request, 'auth/register.html', {'form': form})
        
    else:
        initial_data = {'username':"",'password1':"","password2":""}
        form = UserCreationForm(initial=initial_data)
        return render(request,'auth/register.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("dashboard")
        # return render(request, 'auth/login.html', {'form': form})
        
    else:
        initial_data = {'username':"",'password':""}
        form = AuthenticationForm(initial=initial_data)
    return render(request,'auth/login.html',{'form':form})

def dashboard(request):
    return render(request,'dashboard.html')

def logout_user(request):
    logout(request)
    return redirect('login')