from django.shortcuts import redirect 

def auth(view_functon):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_functon(request,*args,**kwargs)
    return wrapped_view

def guest(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_function(request,*args,**kwargs)
    return wrapped_view