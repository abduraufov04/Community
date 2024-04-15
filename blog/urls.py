from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailDetailView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name="create_blog"),
    path('detail/<int:pk>/', BlogDetailDetailView.as_view(), name = "detail_blog"),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name = "update_blog"),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name = "delete_blog"),
    path('', BlogListView.as_view(), name = 'blog'),
]
