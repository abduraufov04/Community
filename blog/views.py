from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})
    
    
class BlogDetailDetailView(DetailView):
    model = Blog
    template_name='blog_detail.html'
    context_object_name='blog'


class BlogUpdateView(UpdateView):
    model = Blog
    form_class= BlogForm
    template_name = "blog_form.html"
    success_url = reverse_lazy('blog')
    
    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})
    
    
class BlogDeleteView(DeleteView):
    model = Blog
    template_name='delete_confirm.html'
    success_url = reverse_lazy('blog')
