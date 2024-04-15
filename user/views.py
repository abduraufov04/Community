from django.shortcuts import render

from django.views.generic import ListView
from .models import User

class UserListView(ListView):
    model = User
    template_name='list.html'