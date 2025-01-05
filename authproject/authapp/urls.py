from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_user,name='register'),
    path('login/',views.login_user,name='login'),
    path('logut/',views.logout_user,name='logout'),
    path('dashboard/', views.dashboard,name='dashboard')
]