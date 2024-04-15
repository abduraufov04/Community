from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from blog.forms import BlogForm

from .models import Blog

class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name='blog.html'
    
    
class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_form.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog')
    
    
class BlogDetailDetailView(DetailView):
    model = Blog
    template_name='blog_detail.html'
    context_object_name='blog'