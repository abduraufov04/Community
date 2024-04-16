from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .models import User
from .forms import UserForm

class UserListView(ListView):
    model = User
    template_name='list.html'
    
def user_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(user = request.user)
        return render(request, 'auth/profile.html', context={"my_user": user})
    return redirect('login')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "blog_form.html"
    success_url = reverse_lazy('profile')
