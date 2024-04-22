from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment

class BlogListView(ListView):
    context_object_name = 'blogs'
    template_name='blog.html'
    
    def get_queryset(self):
        queryset = Blog.objects.all()

        query = self.request.GET.get('query', '')
        print(98327492837492374293742938, query)
        if query:
            queryset = queryset.filter(type=query)  
        return queryset


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_form.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('detail_blog', kwargs={'pk': self.object.pk})
    
    
class BlogDetailDetailView(DetailView):
    model = Blog
    template_name='blog_detail.html'
    context_object_name='blog'


class BlogUpdateView(UpdateView, LoginRequiredMixin):
    model = Blog
    form_class= BlogForm
    template_name = "blog_form.html"
    success_url = reverse_lazy('blog')
    
    def get_success_url(self):
        return reverse_lazy('detail_blog', kwargs={'pk': self.object.pk})
    
    
class BlogDeleteView(DeleteView, LoginRequiredMixin):
    model = Blog
    template_name='delete_confirm.html'
    success_url = reverse_lazy('blog')


@login_required
def create_comment(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    
    try:
        blog = Blog.objects.get(id = pk)
        comment = request.POST['comment']
        if len(comment ) == 0:
            raise 0/0
        Comment.objects.create(
            blog = blog,
            body = comment,
            author = request.user
        ).save()
        return redirect('detail_blog', pk)
    except:
        return redirect('blog')