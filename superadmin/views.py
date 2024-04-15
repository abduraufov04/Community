from django.shortcuts import render

from django.views.generic import ListView

from admins.models import Admins

class AdminsListView(ListView):
    model = Admins
    template_name = 'list.html'
    

