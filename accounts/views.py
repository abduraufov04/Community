from django.shortcuts import render, redirect
from .forms import UserForm

from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            print(44444444444, request.POST['phonenumber'], request.POST['password'])
            user = authenticate(phonenumber = request.POST['phonenumber'], password =  request.POST['password'])
            print(3333333, user)
            if user:
                login(request, user)
                return redirect('register')
            else:
                return render(request, 'auth/login.html', context={"error": "Something is wrong"})
        return render(request, 'auth/login.html')
    


def user_register(request):
        
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                print(1111111111, form.data)
                user = form.save()
                print(2222222222222222, user)
                return redirect('login')
            return render(request, 'auth/register/html', context=form.errors)
        else:
            return render(request, 'auth/register.html')
