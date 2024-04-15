from django.shortcuts import render, redirect
from .forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.models import User

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user = authenticate(phonenumber = request.POST['phonenumber'], password =  request.POST['password'])
            if user:
                login(request, user)
                return redirect('register')
            else:
                return render(request, 'auth/login.html', context={"error": "Something is wrong"})
        return render(request, 'auth/login.html')
    else:
        if request.user.is_superuser:
            pass
        elif request.user.is_staff:
            pass
        
        return redirect('dashboard')
        
        
def user_register(request):        
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.data['password'])
                user.save()
                
                User.objects.create(user = user).save()
                return redirect('login')
            return render(request, 'auth/register.html', context={"error": form.errors})
        else:
            return render(request, 'auth/register.html')
    return redirect('dashboard')

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')