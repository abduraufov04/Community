from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailDetailView

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name="create_blog"),
    path('detail/<int:pk>/', BlogDetailDetailView.as_view(), name = "detail_blog"),
    path('', BlogListView.as_view(), name = 'blog'),
]
