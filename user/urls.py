from django.urls import path

from .views import UserListView, user_profile, UserUpdateView
urlpatterns = [
    path('user_list/', UserListView.as_view(), name = 'user_list'),
    path('profile/', user_profile, name = "user_profile"),
    path('edit_profile/<int:pk>/', UserUpdateView.as_view(), name = 'edit_user_profile'),
]
